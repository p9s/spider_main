import spidermethod
import time

time1 = time.time()
url = 'https://www.amazon.com/product-reviews/B0066BE3TG/ref=cm_cr_arp_d_paging_btm_1?&sortBy=recent&pageNumber=1'
soup = spidermethod.get_htmlsoup(url)

time2 = time.time()

text = soup.find(class_="a-size-base review-text")

time3 = time.time()

print text.get_text()
print int(time3-time2)
print int(time2-time1)