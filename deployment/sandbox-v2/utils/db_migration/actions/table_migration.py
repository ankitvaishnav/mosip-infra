from db import DatabaseSession
from paths import dmlPath
from utils import getJsonFile, writeJsonFile, myPrint
import config as conf


class TableMigration:
    def __init__(self):
        self.db1: DatabaseSession = DatabaseSession(conf.db_host, conf.db_port, conf.db1_user, conf.db1_pass, conf.db1_name)
        self.db2: DatabaseSession = DatabaseSession(conf.db_host, conf.db_port, conf.db2_user, conf.db2_pass, conf.db2_name)
        return

    def run(self):
        myPrint("Take backup")
        self.db1.copyTable(conf.db1_table, dmlPath)
        myPrint("Take backup finished")

        myPrint("Creating table")
        self.db2.createTable(conf.table_schema)
        myPrint("Creating table finished")

        myPrint("Inserting table")
        self.db2.insertFromCsv(conf.db2_table, dmlPath)
        myPrint("Inserting table finished")