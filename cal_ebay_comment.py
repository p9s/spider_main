import MySQLdb as mydatabase
import time

cursor.execute('SELECT * FROM py_product_comments')
result = cursor.fetchall()
rst = []
for i in result:
    if 'EBCM' in i[12]:
        rst.append(i[1:])

index_dict = {}
for i in rst:
    if i[0] in index_dict:
        index_dict[i[0]] += 1
    else:
        index_dict[i[0]] = 1

for key in index_dict:
        try:
            sql_1 = "UPDATE py_productDynamic SET pro_commentnumber = "+str(index_dict[key])+" WHERE pro_asin = '"+str(key)+"'AND pro_ctime like '%"+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+"%'"
            #print str(key),index_dict[key]
            
            cursor.execute(sql_1)
            
        except Exception,e:
            print str(e)
            continue
    conn.commit()