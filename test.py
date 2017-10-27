import spidermethod

url = 'https://cn.udacity.com/1024/#/debug'
soup = spidermethod.get_htmlsoup(url)
soup = soup.find('body').find('p')
print soup