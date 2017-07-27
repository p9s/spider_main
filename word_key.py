#coding=utf-8
import MySQLdb as mydatabase
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import rake
import nltk
import emotionanalysis
import config

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='dolphin_staff', charset='utf8')
cursor = conn.cursor()


print 'connecting successful...'

cursor.execute('SELECT * FROM comment_from_baleaf')
results = cursor.fetchall()
comment_list = []
for i in results:
    comment_list.append(i)

print 'analyzing...'

def get_key_word(comment_line):
    nltk_keyword = emotionanalysis.get_keyword(comment_line[3])#用nltk提取出评论正文中的关键词
    nltk_keyword = nltk_keyword.lower()#统一处理成小写
    nltk_keyword = nltk_keyword.split(',')#以逗号分割成列表
    
    judge = comment_line[9]
    if int(judge) > 3:
        judge = '1'
    elif int(judge) < 3:
        judge = '-1'
    else:
        judge = '0'
    #此处添加判定，是好评还是差评

    tmp = rake.select_kw(comment_line[3])
    #通过rake提取关键词和关键词评分

    rst_tmp = []
    for j in tmp:
        if float(j[1]) > 1.0 and j[0] not in nltk_keyword:
            #排除掉rake中分数过低的关键词
            rst_tmp.append([j[0],j[1],comment_line[0],comment_line[3],judge,config.good_type])
            #格式化输出结果

#这块代码用来获取关键词       
    return rst_tmp


pool = Pool(6)#开六条进程（动用6cpu处理）
result = pool.map(get_key_word,comment_list)
analys = []
for i in result:
    analys.extend(i)
pool.close()
pool = []
#把处理结果储存起来，然后清空列表

def count_all(analys):
    count_dict_all = {}
    for i in analys:
        if i[0] in count_dict_all:
            count_dict_all[i[0]] += 1
        else:
            count_dict_all[i[0]] = 1
    return count_dict_all
    #获取全部词语


def count_pos(analys):
    count_dict_pos = {}
    for i in analys:
        if str(i[4]) == '1':
            if i[0] in count_dict_pos:
                count_dict_pos[i[0]] += 1
            else:
                count_dict_pos[i[0]] = 1
        else:
            continue
    return count_dict_pos
    #获取正面评论

def count_neg(analys):
    count_dict_neg = {}
    for i in analys:
        if str(i[4]) == '-1':
            if i[0] in count_dict_neg:
                count_dict_neg[i[0]] += 1
            else:
                count_dict_neg[i[0]] = 1
        else:
            continue
    return count_dict_neg
    #获取负面评论

def count_mid(analys):
    count_dict_mid = {}
    for i in analys:
        if str(i[4]) == '0':
            if i[0] in count_dict_mid:
                count_dict_mid[i[0]] += 1
            else:
                count_dict_mid[i[0]] = 1
        else:
            continue
    return count_dict_mid
    #获取中评

def get_word_type(analys):
    word_type_dict = {}
    for i in analys:
        if i[0] not in word_type_dict:
            word_type_dict[i[0]] = nltk.pos_tag([i[0]])
    return word_type_dict
    #获取词语的类型

def get_word_count(analys):
    print 'counting...'
    count_dict_all = count_all(analys)
    count_dict_pos = count_pos(analys)
    count_dict_mid = count_mid(analys)
    count_dict_neg = count_neg(analys)
    word_type_dict = get_word_type(analys)

    result_list = []
    for word in count_dict_all:
        try:
            neg = str(count_dict_neg[word])
        except:
            neg = '0'
        try:
            pos = str(count_dict_pos[word])
        except:
            pos = '0'
        try:
            mid = str(count_dict_mid[word])
        except:
            mid = '0'

        result_tuple = (word,((word_type_dict[word])[0])[1],count_dict_all[word],pos,neg,mid,config.good_type)
        result_list.append(result_tuple)

    result_list = list(set(result_list))
    # conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='db_data2force', charset='utf8')
    # cursor = conn.cursor()


    print 'writing into database...'
    count = 0
    for line in result_list:
        #print line
        cursor.execute('INSERT INTO  py_keyword_word_count (express_without_score,word_type,count_all,count_pos,count_neg,count_mid,good_type)  values(%s,%s,%s,%s,%s,%s,%s)',line) 
        count = count+1
        if count % 10000 == 0:
            conn.commit()#五千条提交一次    
    conn.commit()

def get_main_word():
    get_word_count(analys)

    # conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='db_data2force', charset='utf8')
    # cursor = conn.cursor()

    cursor.execute('SELECT * FROM py_keyword_word_count')
    results = cursor.fetchall()
    print result[2]
    print 'getting main table...'
    index_dict = {}
    for i in results:
        if i[1] not in index_dict:
            index_dict[i[1]] = i[0]

    final_result = []
    for item in analys:
        final_result.append(item+[index_dict[item[0]]])

    count = 0
    for line in final_result:
        #print len(line)
        #print line
        cursor.execute('INSERT INTO  py_keyword_main_tmp (express,score,comment_id,comment,pos_or_neg,good_type,express_id)  values(%s,%s,%s,%s,%s,%s,%s)',line) 
        count = count+1
        if count % 5000 == 0:
            conn.commit()

    conn.commit()


get_main_word()



