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

cursor.execute('SELECT * FROM py_product_comments WHERE good_type = "JY"')#从数据库中提取全部数据
pro_info = cursor.fetchall()
print len(pro_info)

cursor.execute('SELECT * FROM py_keyword_main_tmp WHERE good_type = "JY"')#从数据库中提取全部数据
key_words = cursor.fetchall()
print len(key_words)


key_list = []
for i in key_words:
    tmp = []
    for j in i:
        tmp.append(j)
    key_list.append(tmp[1:])

result = []
for key in key_list:
    pro_index = key[2]
   
    for i in pro_info:
        if int(i[0]) == int(pro_index):
            key.append(i[6])
            
            break
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