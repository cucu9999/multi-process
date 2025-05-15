import queue
import threading
import time 
import random

import blog_spider

def craw_producer(url_queue:queue.Queue, html_queue:queue.Queue):
    '''
    url_queue: 存放待爬取的url
    html_queue: 存放爬取到的html网页内容
    '''
    while 1:
        url = url_queue.get()
        html = blog_spider.craw(url) # 爬取网页
        html_queue.put(html)
        print(
            threading.current_thread().name, f"craw {url}", 
            "url_queue size=", url_queue.qsize()
              )
        # time.sleep(random.random()) # 0-1随机浮点数
        # time.sleep(1)


def parse_consumer(html_queue:queue.Queue, fout):
    while 1:
        html = html_queue.get()
        results = blog_spider.parse(html) # 解析网页
        print(
            threading.current_thread().name, f"result size:{len(results)}",
            f"html_queue size: {html_queue.qsize()}"
        )
        for res in results:
            fout.write(str(res) + "\n")
        # time.sleep(random.random())

if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)
    
    # # producer
    # for i in range(3):
    #     t = threading.Thread(target=craw_producer, args=(url_queue, html_queue))
    #     t.start()
    
    # # consumer
    # fout = open("result.txt", "w")
    # for i in range(2):
    #     t = threading.Thread(target=parse_consumer, args=(html_queue, fout))
    #     t.start()
    
    # producer-consumer --> 5.9s

    fout = open("result.txt", "w")
    while 1:
        print(f"url_queue size: {url_queue.qsize()}")
        results = blog_spider.parse(blog_spider.craw(url_queue.get()))
        # time.sleep(1)
        for res in results:
            fout.write(str(res) + "\n")

    # 串行线程 --> 