#coding=utf-8
import MySQLdb as mydatabase

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='dolphin_staff', charset='utf8')
cursor = conn.cursor()
print 'connecting successful...'

cursor.execute('SELECT * FROM py_product_comments WHERE prod_website = "AZCM"')#从数据库中提取全部数据
cstms = cursor.fetchall()
time_list = []
for item in cstms:
    if int(item[10].split('/')[0])>=2017 and int(item[10].split('/')[1])>=7:
        time_list.append(item)

print len(time_list)
# for i in time_list:

print 'writing'

fh = open('custmer.txt','w')
tmp = []
for i in cstms:
    tmp.append(i[7])

tmp = list(set(tmp))

for i in tmp:
    fh.write(i+'\n')

fh.close()
print len(tmp)

#把用户的地址后缀保存成txt文件，每一行是一个地址后缀