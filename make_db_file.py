# coding=utf-8

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def store_database(db, dbfilename=dbfilename):
    """
        将数据库格式化保存为普通文件
    """

    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)     # <==> dbfile.write(key + '\n')
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB,file=dbfile)
    dbfile.close()


def load_database(dbfilename=dbfilename):
    """
        解析数据,重新构建数据库
    """
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from initdata import db
    store_database(db)









