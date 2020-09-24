#!/usr/bin/env python
# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='WingTsun',
    version="0.1.0",
    description=(
        '可视化训练深度学习，在线浏览器界面框架'
    ),
    long_description=open('README.rst').read(),
    author='liuweinan',
    author_email='liuweinan53@outlook.com',
    maintainer='liuweinan',
    maintainer_email='liuweinan@outlook.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
            'Twisted>=13.1.0',
            'tensorflow-gpu>=1.10.0'
        ],
    entry_points={
        'WingTsun': ['view.cli'],
    },
    scripts=['app.py'],
)

