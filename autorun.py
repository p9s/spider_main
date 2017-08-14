#coding=utf-8
import time
import os
import time
import config

count = 0
while True:
    fh = open('asid_list.txt')
    answer = fh.readline()
    if answer[0] == '' or len(answer) == 0:
        os.system('python get_asin_list.py')
        count+=1
        if count == 10:
            break
    else:
        os.system('python commentspider.py')


os.system('python intodb.py')
os.system('python main_run.py')


