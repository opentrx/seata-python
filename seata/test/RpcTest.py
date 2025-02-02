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

from seata.boot.GlobalTransactionScanner import GlobalTransactionScanner
from seata.config.Configuration import Configuration
from seata.tm.api.DefaultGlobalTransaction import DefaultGlobalTransaction
from seata.tm.api.GlobalTransactionRole import GlobalTransactionRole

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(__file__))
    Configuration(base_dir + '/script/client.yml')
    GlobalTransactionScanner()

    gt = DefaultGlobalTransaction(None, None, GlobalTransactionRole.Launcher)
    gt.begin(60000, "xxx")
    print("xid = [{}]".format(gt.xid))
