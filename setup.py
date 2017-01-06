"""
csvalidate
"""

import os
import subprocess
from setuptools import setup

VERSION_FILE = "version.txt"


def read(fname):
    fullname = os.path.join(os.path.dirname(__file__), fname)
    with open(fullname) as fp:
        content = fp.read()
    return content


def get_version():
    if os.path.isdir(".git"):
        version = subprocess.check_output(["git", "describe", "--tags",
                                           "--always"],
                                          universal_newlines=True)
        version = version[:-1]
        with open(VERSION_FILE, mode='w') as fp:
            fp.write(version)
    else:
        version = read(VERSION_FILE)
    return version


setup(
    name="csvalidate",
    version=get_version(),
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
