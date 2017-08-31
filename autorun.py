#coding=utf-8
import time
import os
import time
import config

fh = open('reault/result_comment.txt','r')
fh.close()

count = 0
while True:
    fh = open('asid_list.txt')
    answer = fh.readline()
    if len(answer) == 0:
        os.system('python get_asin_list.py')
        count+=1
        if count == 10:
            break
    else:
        os.system('python commentspider.py')

os.system('python intodb.py')



