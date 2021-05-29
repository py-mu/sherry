# coding=utf-8
"""
    create by pymu
    on 2021/4/29
    at 16:30
    具体命令详解，请参阅：https://blog.konghy.cn/2018/04/29/setup-dot-py/
"""
import os

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


def gen_data_files(*dirs):
    """获取文件夹下的所有文件枚举"""
    results = []
    for src_dir in dirs:
        results += [os.path.join(root, i) for root, _, files in os.walk(src_dir) for i in files]
    return results


# 打包包内非py文件
package_data = {'sherry': gen_data_files('resource')}
# 打包静态文件
data_files = [('resource', gen_data_files('resource'))]
setup(
    py_modules=['main'],
    classifiers=classifiers,
    packages=find_packages(),
    data_files=data_files,
    # package_data=package_data,
    install_requires=['QtAwesome>=0.7.0', 'PyQt5>=5.12'],
    python_requires='>=3.6',
    **__sherry_info__
    # entry_points={
    #     'console_scripts': [
    #         'eq-manager=EasyQt.manager:main',
    #     ],
    # }
)
