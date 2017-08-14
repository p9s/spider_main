#coding=utf-8
import MySQLdb as mydatabase

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='dolphin_staff', charset='utf8')
cursor = conn.cursor()

cursor.execute('SELECT * FROM user_product WHERE website = "AZCM" AND user_id = 67')#从数据库中提取全部数据
asid_list = cursor.fetchall()


result = []
for i in asid_list:
    asid = i[2]
    try:
        if str(asid)[0] == 'B':
            result.append(asid)
        else:
            continue
    except:
        continue

fh = open('asid_list.txt','w')
for i in result:
    fh.write(str(i.strip()))
    fh.write('\n')

fh.close()


