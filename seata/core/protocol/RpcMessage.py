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

import threading

atom = 0
lock = threading.RLock()


class RpcMessage(object):

    def __init__(self):
        # int
        self.id = 0
        # byte
        self.message_type = 0
        # byte
        self.codec = 0
        # byte
        self.compressor = 0
        # map string, string
        self.head_map = dict()
        # Object
        self.body = None

    @staticmethod
    def get_id():
        global atom, lock
        with lock:
            atom = (atom + 1) & 0x7FFFFFFF
        return atom

    @staticmethod
    def build_request_message(msg, message_type):
        rpc_message = RpcMessage()
        rpc_message.id = RpcMessage.get_id()
        rpc_message.message_type = message_type
        # TODO
        rpc_message.codec = 0x1
        rpc_message.compressor = 0x0
        rpc_message.body = msg
        return rpc_message

    @classmethod
    def build_response_message(cls, rpc_message, msg, message_type):
        rpc_msg = RpcMessage()
        rpc_msg.message_type = message_type
        rpc_msg.codec = rpc_message.codec
        rpc_msg.compressor = rpc_message.compressor
        rpc_msg.body = msg
        rpc_msg.id = rpc_message.id
        return rpc_msg
