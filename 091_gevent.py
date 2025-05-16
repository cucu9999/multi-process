from gevent import monkey
monkey.patch_all()

import time
import blog_spider
import gevent

# sigle thread
start_time = time.time()
for url in blog_spider.urls:
    blog_spider.craw(url)    

end_time = time.time()
print(f"single thread time: {end_time - start_time}s")

# gevent
start_time = time.time()
tasks = [
    gevent.spawn(blog_spider.craw, url)
    for url in blog_spider.urls
]
gevent.joinall(tasks)

end_time = time.time()
print(f"gevent time: {end_time - start_time}s") 
