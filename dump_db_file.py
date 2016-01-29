# coding=utf-8

from make_db_file import load_database

db = load_database()
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])