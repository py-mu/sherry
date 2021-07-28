
<!--suppress HtmlDeprecatedAttribute -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/py-mu/sherry/main/docs/img/icon.png" alt="sherry">
</h1>

<p align="center">
    <a href="https://github.com/py-mu/sherry" target="_blank"><img src="https://img.shields.io/github/workflow/status/py-mu/sherry/Upload%20Python%20Package%20Sherry" alt="auto CI"></a>
    <a href="https://github.com/py-mu/sherry"><img src="https://img.shields.io/github/languages/count/py-mu/sherry" alt="maven-central"></a>
    <img src="https://img.shields.io/pypi/v/sherry" alt="sherry">
    <img src="https://img.shields.io/pypi/pyversions/sherry" alt="python version">
  <a href="https://www.codacy.com/gh/py-mu/sherry/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=py-mu/sherry&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/53ebcd7351bb42eb96d2c9b093ae5007" alt="Codacy Badge"></a>
    <a href="./LICENSE"><img src="https://img.shields.io/github/license/py-mu/sherry" alt="license MIT"></a>
    <a href="https://github.com/py-mu/sherry"><img src="https://img.shields.io/github/stars/py-mu/sherry?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/py-mu/sherry"><img src="https://img.shields.io/github/forks/py-mu/sherry?style=social" alt="GitHub forks"></a>
</p>


# 📑 简介 | Intro

使用PyQt开发桌面应用往往是非专业从事桌面开发的人员，开发桌面客户端也仅是给自己的程序添加面向用户交互，
在不想增加学习成本的前提下，选择哪个哪个开发框架，让人头疼，，如何才能高效的开发出一个符合大众审美的应用程序？那么在原有的Python能力下，结合Sherry的加持，
你也能快速上手并开发出一个让人身心愉悦的应用。此处不应该有对Qt高深的技术实现，如2D、3D等，如果需要，个人建议使用C++及专业的界面开发人员，此仅面向“兼职”的界面开发者。


# 🌌 特性 | Feature

- 布局好，布局方便。
- 依赖性少。
- 高效开发，所见即所得。
- 迭代兼容性。
- 业务逻辑纯粹，界面布局与业务分离。
- 跨平台。

# 🖼 演示截图 | Screenshot

![welcome](https://raw.githubusercontent.com/py-mu/sherry/main/docs/img/welcome.png)

# 🎄 目录结构 | structure

    -sherry                 # 项目目录
        | -docs             # 项目文档
        | -sherry           # 框架主包
            | -core         # 框架核心类
            | -inherit      # Qt系列衍生类
            | -resource     # 框架自带的资源文件夹
            | -utils        # 工具类
            | -variable     # 框架全局变量
            | -view         # 框架内部自带的页面原型即视图
        | -build.bat/sh     # 框架打包脚本
        | -LICENSE          # LICENSE说明
        | -MANIFEST.in      # 框架打包辅助说明
        | -README.md        # 辅助说明
        | -requirements.txt # 依赖列表
        | -setup.py         # 打包入口

# 🚀 快速上手 | Quick start

1. 安装Sherry

```shell
pip install sherry
```

2. 启动

```python
from sherry.core.launcher import Application

if __name__ == '__main__':
    Application().run()
```

3. 使用设计原型

```
# 生成设计原型
# 实例化窗口
# 使用Sherry启动
```

更多请访问[使用文档](https://py-mu.github.io/sherry/)
