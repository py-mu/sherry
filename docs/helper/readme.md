
# 安装

1. pip 安装

```
pip install sherry
```

2. 源码安装（安装最新版）

```
# 下载源码 
git clone git@github.com:py-mu/sherry.git

cd sherry

sh build.sh
或
python setup.py install
```

> import sherry 没有出现异常则说明安装成功，可以开启你的开发之旅了。

# 使用

```python
# encoding=utf-8
"""
    通过 Sherry Application 启动器启动你的任意视图，
    可以是设计原型，也可以是装饰子类，这里不指定启动视图则使用默认欢迎页。
"""
from sherry.core.launcher import Application

if __name__ == '__main__':
    Application().run()

```

# 高级
