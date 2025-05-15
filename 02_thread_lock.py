import threading
import time

class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    if account.balance >= amount:
        time.sleep(0.1)
        account.balance = account.balance - amount
        print(threading.current_thread().name, f"successfully draw,balance:{account.balance}")
    else:
        print(threading.current_thread().name, f"not enough balance")

if __name__ == '__main__':
    account = Account(1000)
    ta = threading.Thread(name='ta', target=draw, args=(account, 800))
    tb = threading.Thread(name='tb', target=draw, args=(account, 800))

    ta.start()
    tb.start()


        
