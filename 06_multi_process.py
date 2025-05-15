import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing
import time


PRIMES = [112272535095293] * 100

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def sigle_thread():
    for n in PRIMES:
        is_prime(n)

def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)

def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)

if __name__ == '__main__':
    # print('Single thread')
    # start_time = time.time()
    # sigle_thread()
    # end_time = time.time()
    # print('Time taken:', end_time - start_time) # 37.48s

    # print('Multi thread')
    # start_time = time.time()
    # multi_thread()
    # end_time = time.time()
    # print('Time taken:', end_time - start_time) # 38.92s

    print('Multi process')
    start_time = time.time()
    multi_process()
    end_time = time.time()
    print('Time taken:', end_time - start_time) # 4.97s