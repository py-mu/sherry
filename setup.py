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
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers'
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: Chinese',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

package_data = {'sherry': ['*.pyi', '*.ui']}
setup(
    platforms=['OS-independent'],
    classifiers=classifiers,
    packages=find_packages(),
    include_package_data=True,
    package_data=package_data,
    install_requires=['QtAwesome>=0.7.0', 'PyQt5>=5.12'],
    python_requires='>=3.6',
    **__sherry_info__
)
