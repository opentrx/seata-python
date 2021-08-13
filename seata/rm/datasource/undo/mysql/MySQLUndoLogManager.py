#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.compressor.CompressorType import CompressorType
from seata.rm.datasource.undo.State import State
from seata.rm.datasource.undo.UndoLogManager import UndoLogManager
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class MySQLUndoLogManager(UndoLogManager):

    @classmethod
    def get_insert_undo_log_sql(cls):
        return "INSERT INTO " + \
               cls.UNDO_LOG_TABLE_NAME + \
               " (branch_id, xid, context, rollback_info, log_status, log_created, log_modified) " + \
               "values (?,?,?,?,?,now(6),now(6))"

    def get_db_type(self):
        return JdbcConstants.MYSQL

    def batch_delete_undo_log(self, xids, branch_ids, connection):
        pass

    def delete_undo_log_by_log_created(self, log_created, limit_rows, connection):
        pass

    def insert_undo_log_with_global_finished(self, xid, branch_id, undo_log_parser, connection):
        self.insert_undo_log(xid, branch_id, self.build_context(undo_log_parser.get_name(), CompressorType.NONE),
                             undo_log_parser.get_default_content(), State.GlobalFinished, connection)

    def insert_undo_log_with_normal(self, xid, branch_id, rollback_context, undo_log_content, connection):
        self.insert_undo_log(xid, branch_id, rollback_context, undo_log_content, State.Normal, connection)

    def insert_undo_log(self, xid, branch_id, rollback_context, undo_log_content, state, connection):
        try:
            cursor = connection.cursor()
            cursor.execute(self.get_insert_undo_log_sql(),
                           (branch_id, xid, rollback_context, undo_log_content, state.value))
            connection.commit()
        except Exception as e:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception as ignored:
                    pass
