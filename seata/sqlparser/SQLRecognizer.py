#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.NeedSubclassImplemented import NeedSubclassImplemented


class SQLRecognizer(object):

    def get_sql_type(self):
        raise NeedSubclassImplemented()

    def get_table_alias(self):
        raise NeedSubclassImplemented()

    def get_table_name(self):
        raise NeedSubclassImplemented()

    def get_original_sql(self):
        raise NeedSubclassImplemented()
