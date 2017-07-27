import spidermethod

from multiprocessing.dummy import Pool as ThreadPool

def bug(url):
    while 1:
        spidermethod.get_htmlsoup(url)
        print 'successful'

url = ['http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio','http://fafu.gayhub.studio']
pool = ThreadPool(50)
pool.map(bug,url)

