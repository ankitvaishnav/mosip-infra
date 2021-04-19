import csv
import logging
import sys

import psycopg2
from psycopg2.extras import RealDictCursor, LoggingConnection
import config as conf


class DatabaseSession:
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = self.createConnection(host, port, user, pwd, db)
        self.conn.autocommit = True
        self.conn.initialize(logging)

    @staticmethod
    def createConnection(host, port, user, pwd, db):
        return psycopg2.connect(
            connection_factory=LoggingConnection,
            host=host,
            port=port,
            database=db,
            user=user,
            password=pwd
        )

    def createTable(self, data):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(data)
        cur.close()

    def copyTable(self, table_name, path):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        with open(path, "w") as file:
            cur.copy_to(file, table_name)
            # cur.copy_expert("COPY (SELECT * FROM %s) TO STDOUT WITH CSV HEADER" % table_name, file)

    def insertFromCsv(self, table_name, path):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        f = open(path, 'r')
        cur.copy_from(f, table_name)
        f.close()

    def closeAll(self):
        self.conn.close()
