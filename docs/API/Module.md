----
# Module
----
在PaddleHub中，Module代表了一个`可执行`的模型。这里的可执行指的是，Module可以直接通过命令行`hub run ${MODULE_NAME}`执行预测，或者通过context接口获取上下文后进行finetune。

## `class paddlehub.module.Module(name=None, module_dir=None)`
在生成一个Module时，支持通过名称、url或者路径创建Module
> ### 参数
> * name: 模块名称
>
> * module_dir: 模块路径
>
> ### 返回
> Module
>
> ### 示例
>
> ```python
> import paddlehub as hub
> # 根据模型名字创建Module
> hub.Module(name = "lac")
> ```

## `context(for_test=False, trainable=False, regularizer=None, learning_rate=1e-3)`
用于获取Module的上下文信息，得到输入、输出以及预训练的Paddle Program副本
> ### 参数
> * for_test: 是否用于测试，如果是用于预测，则设置为True，如果用于finetune，则设置为False。默认情况下，该参数被设置为False
>
> * trainable: 获取的Program副本中的参数是否为可训练的，设置为True表示可训练。默认情况下，该参数被设置为False
>
> * regularizer: 获取的Program副本中的参数的正则化项。默认情况下，该参数被设置为None
>
> * learning_rate: 获取的Program副本中的参数的学习率。默认情况下，该参数被设置为1e-3
>
> ### 示例
>
> ```python
> import paddlehub as hub
> resnet = hub.Module(name = "resnet_v2_50_imagenet")
> input_dict, output_dict, program = resnet.context(trainable=True)
> with fluid.program_guard(program):
>     label = fluid.layers.data(name="label", dtype="int64", shape=[1])
>     img = input_dict["image"]
>     feature_map = output_dict["feature_map"]
>     feed_list = [img.name, label.name]
>     fc = fluid.layers.fc(input = feature_map, size = 2)
>     feed_list = [img.name, label.name]
>     # 添加fc层后，进行训练
>     ...
> ```
