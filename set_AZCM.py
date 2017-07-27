#coding=utf-8
import MySQLdb as mydatabase

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='dolphin_staff', charset='utf8')
cursor = conn.cursor()
print 'connecting successful...'

# sql_1 = 'CREATE TABLE py_keyword_dictionary_main_tmp (id INT(11)primary key auto_increment ,express VARCHAR(200),score TEXT(100),comment_id INT(10),comment TEXT(100000),pos_or_neg VARCHAR(10),good_type VARCHAR(100), express_id INT(20),asin VARCHAR(20))'
# try:
#     cursor.execute(sql_1)
# except:
#     print 'table exists'

cursor.execute('SELECT * FROM py_shoes_comment_raw_data WHERE good_type = "JY"')#从数据库中提取全部数据
pro_info = cursor.fetchall()

cursor.execute('SELECT * FROM py_keyword_main_tmp WHERE good_type = "JY" ')#从数据库中提取全部数据
key_words = cursor.fetchall()


key_list = []
for i in key_words:
    tmp = []
    for j in i:
        tmp.append(j)
    key_list.append(tmp[1:])

result = []
for key in key_list:
   pro_index = key_list.index(key)
   #print pro_index
   pro_line = pro_info[pro_index]
   key.append(pro_line[6])
   result.append(key)

print 'writing into database...'

print result[4]
count = 0
for line in result:
    #print line
    cursor.execute('INSERT INTO  py_keyword_main(express,score,comment_id,comment,pos_or_neg,good_type,express_id,prod_asin)  values(%s,%s,%s,%s,%s,%s,%s,%s)',line) 
    count += 1
    if count % 1000 == 0:
        conn.commit()
    else:
        continue

conn.commit() 