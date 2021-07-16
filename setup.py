# coding=utf-8
"""
    create by pymu
    on 2021/4/29
    at 16:30
    具体命令详解，请参阅：https://blog.konghy.cn/2018/04/29/setup-dot-py/
"""

from setuptools import setup, find_packages

from sherry import __sherry_info__

# 分类信息
classifiers = [
    # 发展时期,常见的如下
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',
    # 开发的目标用户
    'Intended Audience :: Developers',
    # 属于什么类型
    'Topic :: Software Development :: Build Tools',
    # 许可证信息
    'License :: OSI Approved :: MIT License',
    # 目标 Python 版本
    'Programming Language :: Python :: 3',
]

setup(
    platforms=['OS-independent'],
    classifiers=classifiers,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['QtAwesome>=0.7.0', 'PyQt5>=5.12'],
    python_requires='>=3.5',
    **__sherry_info__
)
