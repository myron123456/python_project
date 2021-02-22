import re
import pymysql

def write_to_mysql1(target):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='myron123',
        database='crawel'
    )
    cursor = db.cursor()
    sql = "insert into xila_dl(target) values('{}')".format(target)
    cursor.execute(sql)
    print('插入成功')
    db.commit()

def write_to_mysql2(target):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='myron123',
        database='crawel'
    )
    cursor = db.cursor()
    sql = "insert into xila_ndl(target) values('{}')".format(target)
    cursor.execute(sql)
    print('插入成功')
    db.commit()

def read_txt():
    filename = r'../xila_ndl.txt'
    # 按行读取txt文本文档
    with open(filename, 'r', encoding='utf-8') as f:
        datas = f.readlines()
    # 遍历文件
    for data in datas:
        txt = re.split(r'\t|\n', data)[0]
        write_to_mysql2(txt)
        # print(txt)


read_txt()