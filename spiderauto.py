import time
import os

while 1:
    localtime = time.asctime( time.localtime(time.time()) )
    if localtime.split()[3].split(':')[0] == '19':
        os.system('python autorun.py')
        time.sleep(3600)
    time.sleep(60)