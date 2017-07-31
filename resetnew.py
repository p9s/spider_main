import MySQLdb as mydatabase

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='dolphin_staff', charset='utf8')
cursor = conn.cursor()

cursor.execute('SELECT * FROM py_product_comments')
result = cursor.fetchall()
rst = []
for i in result:
    rst.append(i[1:])

cursor.execute('SELECT * FROM py_product_comments_tmp')
new = cursor.fetchall()
nw = []
for i in new:
    nw.append(i[1:])

nw = list(set(new))

def reset_list(new,old):
    write_in = []
    for line in new:
        if line in old:
            continue
        else:
            write_in.append(line)

    return write_in

def count_increase(write_in):
    index_dict = {}
    for i in write_in:
        if i[0] in index_dict:
            index_dict[i[0]] += 1
        else:
            index_dict[i[0]] = 1

    return index_dict


def write_in_database(write_in):
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

def write_increase(index_dict):
    for key in index_dict:
        try:
            sql_1 = "UPDATE py_productDynamic SET pro_commentincrement = "+index_dict[key]+" WHERE pro_asin = '"+str(key)+"'"
            #print str(key),index_dict[key]
            sql_2 = "UPDATE py_productDynamic SET pro_salesvolume = "+(((index_dict[key])**2)/(random.randint(0,index_dict[key]/2)))+" WHERE pro_asin = '"+str(key)+"'"
            
            cursor.execute(sql_1)
            cursor.execute(sql_2)
        except Exception,e:
            print str(e)
            continue
    conn.commit()


write_in = reset_list(nw,rst)
print 'reset finished'
index_dict = count_increase(write_in)
print 'writing into database'
write_increase(index_dict)
#write_in_database(write_in)
