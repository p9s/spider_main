#coding=utf-8
import MySQLdb as mydatabase
import user_agents
import random
import time
import config
import spidermethod
import dbmethod
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 

#keyword = '_'.join(config.keyword_db)+'_tmp'

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='dolphin_staff', charset='utf8')
cursor = conn.cursor()

try:
    sql = """CREATE TABLE comment_from_baleaf_JP(id INT(11)primary key auto_increment ,prod_asin VARCHAR(200),title TEXT(10000),content TEXT(10000),user_name VARCHAR(200),color TEXT(1000),type_call VARCHAR(200),user_address TEXT(1000),vote INT(11),prod_star VARCHAR(200),create_date VARCHAR(200))"""
    cursor.execute(sql)

except:
    print 'table is alredy exist' 

#先读取数据库，建表


file_name = config.keyword_db

comment_list = dbmethod.combination(file_name)

Pool = Pool(2)

comment_list = Pool.map(dbmethod.set_color,comment_list)

comment_list = spidermethod.reset_list(comment_list)
#对内容进行去重

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='db_data2force', charset='utf8')
cursor = conn.cursor()

dbmethod.write_into_database(comment_list,cursor,conn)


conn.commit()

