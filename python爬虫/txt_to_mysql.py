# 该文件主要实现将txt文件传入mysql数据库
import pymysql
import re
import json

# 变量初始化
con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd=' ',
    db=' ',
    charset='utf8',
)


def insert(con, id, image, title, actor, time, score):
    # 数据库游标！
    cue = con.cursor()
    # print("mysql connect succes")  # 测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
    # try-except捕获执行异常
    print('insert into my_100 (id,image,title,actor,time,score) values("{}","{}","{}","{}","{}","{}")'.format(
        id, image, title, actor, time, score))
    try:
        cue.execute(
            'insert into my_100 (id,image,title,actor,time,score) values("{}","{}","{}","{}","{}","{}")'.format(id,
                                                                                                                image,
                                                                                                                title,
                                                                                                                actor,
                                                                                                                time,
                                                                                                                score))
        # 执行sql语句
        # print("insert success")  # 测试语句
    except Exception as e:
        print('Insert error:', e)
        con.rollback()
        # 报错反馈
    else:
        con.commit()
        # 真正的执行语句


def read():
    filename = r'result.txt'
    # 按行读取txt文本文档
    with open(filename, 'r', encoding='utf-8') as f:
        datas = f.readlines()
    # 遍历文件
    for data in datas:
        txt = re.split(r'\t|\n', data)[0]
        txt = json.loads(txt)
        id = txt['index']
        image = txt['image']
        title = txt['title']
        actor = txt['actor'].replace(",", "--")
        time = txt['time']
        score = txt['score']
        insert(con, id, image, title, actor, time, score)
        # 调用insert方法
    print("数据插入完成！")


read()
# 执行read函数
con.close()
# 关闭连接
