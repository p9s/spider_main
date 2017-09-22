import time
import os

while 1:
    localtime = time.asctime( time.localtime(time.time()) )
    if localtime.split()[3].split(':')[0] == '23':
        os.system('python washdb.py')
        os.system('python resetnew.py')
        os.system('python word_key.py')
        os.system('python set_AZCM.py')
        os.system('python word_count_key.py')
        time.sleep(3600)
    time.sleep(60)

