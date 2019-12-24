#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.config import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import logging
import psycopg2


class BaseDao:

    def __init__(self):
        db_host = config.db_host
        db_dbname = config.db_name
        db_user = config.db_user
        db_password = config.db_password
        db_port = config.db_port
        self.db_schema = config.db_schema
        
        self.str_conn = f"""host={db_host} 
            port={db_port}
            dbname={db_dbname}
            user={db_user}
            password={db_password}"""

        logging.basicConfig(format='''%(asctime)s %(levelname)s: %(message)s''',
            level=logging.INFO)

        try:
            self.conn = psycopg2.connect(self.str_conn)
            self.cursor = self.conn.cursor()
        except Exception as err:
            logging.error("Falha na tentativa de conexão com o banco!")
            logging.error(f"Erro: {err}")
            raise err

    def commit(self):
        try:
            self.conn.commit()
        except Exception as err:
            logging.error("Falha no commit da transação!")
            logging.error(f"Erro: {err}")
            raise err

    def close(self):
        self.cursor.close()
        self.conn.close()

    def rollback(self):
        try:
            self.conn.rollback()
        except Exception as err:
            logging.error("Falha no rollback da transação!")
            logging.error(f"Erro: {err}")
            raise err

    def execute(self, sql, vars=None):
        try:
            self.cursor.execute(sql, vars)
        except Exception as exc:
            logging.error("Falha na execução de código SQL!")
            logging.error(f"Erro: {exc}")
            self.conn = psycopg2.connect(self.str_conn)
            self.cursor = self.conn.cursor()
            raise(exc)

    def fetchall(self, sql, vars=None, notransaction=True):
        try:
            if notransaction:
                self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor.execute(sql, vars)
            result_set = self.cursor.fetchall()
            return result_set
        except Exception as err:
            logging.error("Falha em consulta ao banco!")
            logging.error(f"Erro: {err}")
            self.conn = psycopg2.connect(self.str_conn)
            self.cursor = self.conn.cursor()
            return None

    def fetchone(self, sql, vars=None, notransaction=True):
        try:
            if notransaction:
                self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor.execute(sql, vars)
            result = self.cursor.fetchone()
            return result
        except Exception as err:
            logging.error("Falha em consulta ao banco!")
            logging.error(f"Erro: {err}")
            self.conn = psycopg2.connect(self.str_conn)
            self.cursor = self.conn.cursor()
            return None
