# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import os

import setuptools

VERSION = "0.1"

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, "README.md"), "r") as f:
    long_description = f.read()

with open(os.path.join(base_dir, "requirements.txt"), "r") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="seata-python",
    version=VERSION,
    author="jsbxyyx",
    author_email="jsbxyyx@163.com",
    description="seata-python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    install_requires=install_requires,
    url="https://github.com/opentrx/seata-python",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
