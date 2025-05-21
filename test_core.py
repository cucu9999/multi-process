'''
多线程中，关于 CPU多核心 调用的测试。
多进程中，关于 CPU多核心 调用的测试。
'''

import psutil
p = psutil.Process()
p.cpu_affinity([0, 1, 2, 3])  # 允许运行在 CPU 0-3 上


'''
多进程中，每个进程对应一个核心运行。超载时，系统仍然会进行调度进行上下文切换。
'''
import multiprocessing
import os
import time
import psutil

def io_bound_task():
    core = psutil.Process(os.getpid()).cpu_num()
    print(f"Process {os.getpid()} running on core {core}")
    time.sleep(2)  # 保持运行一段时间

def cpu_bound_task():
    x = 0
    for _ in range(1000000):
        x += 1
        if _ % 1000000 == 0:
            print(f"Process ID: {os.getpid()} running on CPU: {psutil.Process().cpu_num()}")

if __name__ == '__main__':

    t1 = time.time()

    processes = []
    for _ in range(5):  # 创建 5 个进程
        p = multiprocessing.Process(target=cpu_bound_task)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    t2 = time.time()
    print(f"Total time: {t2 - t1}")

