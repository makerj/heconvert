""" Setup for heconvert """
import os

from setuptools import setup, find_packages


def reads(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf8').read()
    except IOError:
        return ''


setup(
    name='heconvert',
    version='1.0.2',
    description='simple converter that converts hangul to english and vise versa',
    long_description=reads('README.rst'),
    license=reads('LICENSE'),

    author="makerj",
    author_email="ohenwkgdj@gmail.com",
    url="https://github.com/makerj/heconvert",

    keywords=['hangul', 'converter'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],

    packages=find_packages(),
    install_requires=[],
)
