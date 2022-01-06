<!--suppress HtmlDeprecatedAttribute -->
<h1 align="center">
  <img src="https://sherry-docs.vercel.app/resource/image/icon.png" alt="sherry">
</h1>

<p align="center">
    <a href="https://github.com/py-mu/sherry" target="_blank"><img src="https://img.shields.io/github/workflow/status/py-mu/sherry/Upload%20Python%20Package%20Sherry" alt="auto CI"></a>
    <img src="https://img.shields.io/pypi/v/sherry" alt="sherry">
    <img src="https://img.shields.io/pypi/pyversions/sherry" alt="python version">
    <a href="./LICENSE"><img src="https://img.shields.io/github/license/py-mu/sherry" alt="license MIT"></a>
    <a href="https://github.com/py-mu/sherry"><img src="https://img.shields.io/github/stars/py-mu/sherry?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/py-mu/sherry"><img src="https://img.shields.io/github/forks/py-mu/sherry?style=social" alt="GitHub forks"></a>
</p>

# 📑 简介 | Intro

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dda0a3cb721f4f92b1c3ba7aac4f5178)](https://app.codacy.com/gh/py-mu/sherry?utm_source=github.com&utm_medium=referral&utm_content=py-mu/sherry&utm_campaign=Badge_Grade_Settings)

Easy Qt For Python（Sherry） 致力于样式跟界面布局之上，力达能够做出一个用于快速开发的脚手架，适用场景主要：个人学习及脚本图形化，不推荐用于生产开发。

# 🎯 特性 | Feature

- 布局好，布局方便。
- 依赖性少。
- 高效开发，所见即所得。
- 迭代兼容性。
- 业务逻辑纯粹，界面布局与业务分离。
- 跨平台。

# 📷 演示截图 | Screenshot

![welcome](https://sherry-docs.vercel.app/resource/image/welcome.png)

# 🎄 目录结构 | structure

    -sherry                 # 项目目录
        | -sherry           # 框架主包
            | -core         # 框架核心类
            | -inherit      # Qt系列衍生类
            | -resource     # 框架自带的资源文件夹
            | -utils        # 工具类
            | -variable     # 框架全局变量
            | -view         # 框架内部自带的页面原型及视图
        | -build.bat/sh     # 框架打包脚本
        | -LICENSE          # LICENSE说明
        | -MANIFEST.in      # 框架打包辅助说明
        | -README.md        # 辅助说明
        | -requirements.txt # 依赖列表
        | -setup.py         # 打包入口

# 🚀 快速上手 | Quick start

- 安装Sherry

```shell
pip install sherry
```

- 启动

```python
from sherry.core.launcher import Application

if __name__ == '__main__':
    Application().run()
```

更多请访问[使用文档](https://sherry-docs.vercel.app/)
