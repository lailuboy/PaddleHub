# PaddleHub

[![Build Status](https://travis-ci.org/PaddlePaddle/PaddleHub.svg?branch=develop)](https://travis-ci.org/PaddlePaddle/PaddleHub)
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)
[![Version](https://img.shields.io/github/release/PaddlePaddle/PaddleHub.svg)](https://github.com/PaddlePaddle/PaddleHub/releases)

PaddleHub是基于PaddlePaddle开发的预训练模型管理工具，可以借助预训练模型更便捷地开展迁移学习工作。

## 特性

通过PaddleHub，您可以：

1. 通过命令行，无需编写代码，一键使用预训练模型进行预测；
2. 通过hub download命令，快速地获取PaddlePaddle生态下的所有预训练模型；
3. 借助PaddleHub Finetune API，使用少量代码完成迁移学习；
   - 更多Demo可参考 [ERNIE文本分类](https://github.com/PaddlePaddle/PaddleHub/tree/develop/demo/text-classification) [图像分类迁移](https://github.com/PaddlePaddle/PaddleHub/tree/develop/demo/image-classification)

## 安装

**环境依赖**
* Python>=2.7
* PaddlePaddle>=1.3.2

**NOTE:** PaddleHub推荐在Python 3环境下进行使用

pip安装方式如下：

```shell
$ pip install paddlehub
```

**NOTE:** 若出现找不到PaddleHub的错误，请尝试指定pypi源进行安装
```shell
$ pip install -i https://pypi.org/simple/ paddlehub
```

## 快速体验

安装成功后，执行下面的命令，可以快速体验PaddleHub的一键预测功能

```shell
# 使用百度LAC词法分析工具进行分词
$ hub run lac --input_text "今天是个好日子"

# 使用百度Senta情感分析模型对句子进行预测
$ hub run senta --input_text "今天是个好日子"
```

想了解更多PaddleHub已经发布的模型，请使用`hub search`命令查看所有已发布的模型。

```shell
$ hub search
```

## 深入了解PaddleHub
* [命令行功能](https://github.com/PaddlePaddle/PaddleHub/tree/develop/docs/command_line_introduction.md)
* [Finetune API与迁移学习](https://github.com/PaddlePaddle/PaddleHub/tree/develop/docs/tutorial/transfer_learning_tutorial.md)
* [API](https://github.com/PaddlePaddle/PaddleHub/tree/develop/docs/API_list.md)

## 答疑

当安装或者使用遇到问题时，可以通过[FAQ](https://github.com/PaddlePaddle/PaddleHub/blob/develop/docs/FAQ.md)查找解决方案。
如果在FAQ中没有找到解决方案，欢迎您将问题和bug报告以[Github Issues](https://github.com/PaddlePaddle/PaddleHub/issues)的形式提交

## 版权和许可证
PaddleHub由[Apache-2.0 license](LICENSE)提供
