#coding=utf-8
import MySQLdb as mydatabase

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='dolphin_staff', charset='utf8')
cursor = conn.cursor()

cursor.execute('SELECT * FROM py_product_comments_tmp')

result = cursor.fetchall()

result_list = []
for i in result:
    result_list.append(i[1:-1])
tmp = list(set(result_list))
print tmp[10]
#cursor.execute('DELETE FROM py_product_comments_tmp')


count=0
print 'committing'
for line in tmp:
    if line[-1] != u'商品类型':
        try:
            cursor.execute('INSERT INTO py_product_comments(prod_asin,title,content,user_name,color,type_call,user_address,vote,prod_star,create_date,prod_website,prod_group_number,good_type)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',line) 
            count+= 1
            if count%10000 == 0:
                conn.commit()
        except Exception,e:
            print e
            print line
            continue

conn.commit()
