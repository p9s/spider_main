import MySQLdb as mydatabase

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='dolphin_staff', charset='utf8')
cursor = conn.cursor()

cursor.execute('SELECT * FROM product_comments')
result = cursor.fetchall()
rst = []
for i in result:
	rst.append(i[1:])

cursor.execute('SELECT * FROM product_comments_tmp')
new = cursor.fetchall()
nw = []
for i in new:
	nw.append(i[1:])

write_in = []
for line in nw:
	if line in rst:
		continue
	else:
		write_in.append(line)

print 'committing'
for line in write_in:
    try:
        cursor.execute('INSERT INTO py_product_comments(prod_asin,prod_website,prod_group_number,title,content,user_name,color,type_call,user_address,vote,prod_star,create_date,syn_status,good_type)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',line) 
        count+= 1
        if count%10000 == 0:
            conn.commit()
    except:
        print line
        continue

conn.commit()


