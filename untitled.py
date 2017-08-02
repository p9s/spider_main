#coding=utf-8
import MySQLdb as mydatabase

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='dolphin_staff', charset='utf8')
cursor = conn.cursor()

cursor.execute('SELECT * FROM py_productDynamic WHERE pro_asin = "B06ZZRRB6Q" ')#从数据库中提取全部数据
asid_list = cursor.fetchall()

for i in asid_list:
	print i