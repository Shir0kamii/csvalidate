"""
csvalidate
"""

import os
from setuptools import setup


def read(fname):
    fullname = os.path.join(os.path.dirname(__file__), fname)
    with open(fullname) as fp:
        content = fp.read()
    return content


setup(
    name="csvalidate",
    version="1.1.1",
    author="Shir0kamii",
    author_email="shir0kamii@gmail.com",
    description="CSV reader and writer with validation",
    long_description=read("README.rst"),
    url="https://github.com/Shir0kamii/csvalidate",
    download_url="https://github.com/Shir0kamii/csvalidate/tags",
    platforms="any",
    packages=["csvalidate"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
