# coding=utf-8
"""
    create by pymu
    on 2021/4/29
    at 16:30
    具体命令详解，请参阅：https://blog.konghy.cn/2018/04/29/setup-dot-py/
"""

from setuptools import setup, find_packages

from sherry import __sherry_info__

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    long_description_content_type="text/markdown",
    long_description=long_description,
    platforms=['OS-independent'],
    classifiers=classifiers,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['QtAwesome>=0.7.0', 'PyQt5>=5.12'],
    python_requires='>=3.5',
    **__sherry_info__
)
