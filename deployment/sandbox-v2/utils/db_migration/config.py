import os

debug = True if os.getenv("rps_debug") == 'y' else False

# Database
db_host = os.getenv("tm_db_host")
db_port = os.getenv("tm_db_port")

db1_user = os.getenv("tm_db1_user")
db1_pass = os.getenv("tm_db1_pass")
db1_name = os.getenv("tm_db1_name")
db1_table = os.getenv("tm_db1_table")

db2_user = os.getenv("tm_db2_user")
db2_pass = os.getenv("tm_db2_pass")
db2_name = os.getenv("tm_db2_name")
db2_table = os.getenv("tm_db2_table")

table_schema = os.getenv("tm_table_schema")

# JSON print related
json_sort_keys = True
json_indent = 4
