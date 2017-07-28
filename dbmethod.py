#coding=utf-8
import MySQLdb as mydatabase
import config



def combination(keywords):
    rst = []
    for i in keywords:
        fh = open('result/'+i+'result_comment.txt')
        comment_list = fh.readlines()
        rst.extend(comment_list)
    return rst
    #把几个评论列表连接起来，变成一个巨大的列表

def set_color(line):

    try:
        line = (line.strip()).decode('utf-8')
        result_data = line.split('\t')
        #print result_data
        tmp = result_data[4]

        
        tmp = tmp.split('|')
        for i in tmp:
            if 'Color' in i:
                color = i.split(':')
        #对类型切片后进行关键词匹配
        result_data[4] = color[1]
        #result.append(result_data)
    except:
        result_data = []
    
    return result_data
    #重设颜色格式，只留下颜色信息

def write_into_database(comment_list,cursor,conn):
    count = 0 
    for line in comment_list:
        if len(line) != 10:
            continue
        else:
            line.append(config.good_type)
            line.append(config.pro_website)
            line.append(line[0])
            #try:
     
            cursor.execute('INSERT INTO py_product_comments(prod_asin,title,content,user_name,color,type_call,user_address,vote,prod_star,create_date,good_type,prod_website,prod_group_number)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',line) 
            #cursor.execute('INSERT INTO fashion_shoe_comment_tmp (prod_asin,title,content,user_name,color,type_call,user_address,vote,prod_star,create_date)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',line)
            #写入数据库
            count = count + 1           
            # except:
            #     print line
            #     continue
        #写入数据库
        if count%50 == 0:
            conn.commit()

    conn.commit()