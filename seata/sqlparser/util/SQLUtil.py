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

from seata.rm.datasource.ColumnUtils import ColumnUtils


class SQLUtil:

    @classmethod
    def get_db_type(cls, connection):
        # the connection from connection_proxy has db_type, database
        db_type = connection.db_type
        return db_type

    @classmethod
    def build_where_condition_by_pks(cls, pk_column_name_list, row_size, db_type):
        max_in_size = 1000
        where_str = ""
        if row_size % max_in_size == 0:
            batch_size = row_size // max_in_size
        else:
            batch_size = row_size // max_in_size + 1
        for batch in range(batch_size):
            if batch > 0:
                where_str += " OR "
            where_str += "("
            for i in range(len(pk_column_name_list)):
                if i > 0:
                    where_str += ","
                where_str += ColumnUtils.add_by_col_dbtype(pk_column_name_list[i], db_type)
            where_str += ") IN ( "
            if batch == batch_size - 1:
                if row_size % max_in_size == 0:
                    each_size = max_in_size
                else:
                    each_size = row_size % max_in_size
            else:
                each_size = max_in_size
            for i in range(each_size):
                if i > 0:
                    where_str += ","
                where_str += "("
                for x in range(len(pk_column_name_list)):
                    if x > 0:
                        where_str += ","
                    where_str += "%s"
                where_str += ")"
            where_str += ")"
        return where_str

    @classmethod
    def build_where_condition_by_pks_single(cls, pk_name_list, db_type):
        where_str = ""
        for i in range(len(pk_name_list)):
            if i > 0:
                where_str += " AND "
            pk_name = pk_name_list[i]
            where_str += ColumnUtils.add_by_col_dbtype(pk_name, db_type)
            where_str += " = %s "
        return where_str

    @classmethod
    def set_param_for_pk(cls, pk_rows_list, pk_column_name_list):
        params = []
        for pk_rows_idx, pk_rows in enumerate(pk_rows_list):
            for col_idx, column in enumerate(pk_column_name_list):
                f = pk_rows[column]
                params.append(f.get_value())
        return params
