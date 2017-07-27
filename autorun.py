#coding=utf-8
import time
import os
import time
import config


while True:
    not_null = []
    for i in config.keyword:
        fh = open(i+'asid_list.txt')
        content = fh.readlines()#获取asin列表，如果asin列表不存在，就先获取
        if len(content) != 0:
            not_null.append(i)
    fh.close()
    #读取几个文件，看看文件内容，把写完的文件剔除掉，留下还没写完的

    dir_name = config.dir_name
    fh = open('config.py','w')
    content = '","'.join(not_null)
    fh.write('keyword = ["'+content+'"]')
    fh.write('\n')
    fh.write('dir_name = "'+dir_name+'"'+'\n')
    fh.write('keyword_db = ["tmp_"]'+'\n')
    fh.write('good_type = "JY"')
    fh.close()
    #更新配置文件内容

    time.sleep(3)
    os.system('python commentspider.py')
    
    fh.close()
    if dir_name[0] == '':
        break

os.system('python intodb.py')
os.system('python dbreset.py')

