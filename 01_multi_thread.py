import blog_spider
import threading
import time


# urls = [
#     f"专注于为开发者服务，帮助开发者用代码改变世界"
#     for page in range(1, 101)
# ]

def sigle_thread_craw():
    print("single_thread_craw start")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single_thread_craw end")

def multi_thread_craw():
    print("multi_thread_craw start")
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args = (url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("multi_thread_craw end")

if __name__ == '__main__':
    t1 = time.time()
    sigle_thread_craw()
    t2 = time.time()
    print("single_thread_craw time:", t2 - t1) # 14.1s  10.0s

    t1 = time.time()
    multi_thread_craw()
    t2 = time.time()
    print("multi_thread_craw time:", t2 - t1) # 5.3s  1.2s