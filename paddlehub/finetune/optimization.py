#   Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Optimization and learning rate scheduling."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import paddle.fluid as fluid


def adam_weight_decay_optimization(loss,
                                   warmup_steps,
                                   num_train_steps,
                                   learning_rate,
                                   main_program,
                                   weight_decay,
                                   scheduler='linear_decay'):
    if warmup_steps > 0:
        if scheduler == 'noam_decay':
            scheduled_lr = fluid.layers.learning_rate_scheduler\
             .noam_decay(1/(warmup_steps *(learning_rate ** 2)),
                         warmup_steps)
        elif scheduler == 'linear_decay':
            scheduled_lr = linear_warmup_decay(learning_rate, warmup_steps,
                                               num_train_steps)
        else:
            raise ValueError("Unkown learning rate scheduler, should be "
                             "'noam_decay' or 'linear_decay'")
        optimizer = fluid.optimizer.Adam(learning_rate=scheduled_lr)
    else:
        optimizer = fluid.optimizer.Adam(learning_rate=learning_rate)
        scheduled_lr = learning_rate

    clip_norm_thres = 1.0
    fluid.clip.set_gradient_clip(
        clip=fluid.clip.GradientClipByGlobalNorm(clip_norm=clip_norm_thres))

    def exclude_from_weight_decay(name):
        if name.find("layer_norm") > -1:
            return True
        bias_suffix = ["_bias", "_b", ".b_0"]
        for suffix in bias_suffix:
            if name.endswith(suffix):
                return True
        return False

    param_list = dict()

    for param in main_program.global_block().all_parameters():
        param_list[param.name] = param * 1.0
        param_list[param.name].stop_gradient = True

    _, param_grads = optimizer.minimize(loss)

    if weight_decay > 0:
        for param, grad in param_grads:
            if exclude_from_weight_decay(param.name):
                continue
            with param.block.program._optimized_guard(
                [param, grad]), fluid.framework.name_scope("weight_decay"):
                updated_param = param - param_list[
                    param.name] * weight_decay * scheduled_lr
                fluid.layers.assign(output=param, input=updated_param)

    return scheduled_lr
