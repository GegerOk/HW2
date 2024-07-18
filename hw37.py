import threading
from threading import Lock

lock = Lock()

class BankAccount():
    def __init__(self):
        self.balance = 1000
        print(self.balance)

    def up(self, summ):
        with lock:
            for i in range(5):
                self.balance += summ
                print(self.balance)

    def down(self, summ):
        with lock:
            for i in range(5):
                self.balance -= summ
                print(self.balance)

account = BankAccount()

thr1 = threading.Thread(target=account.up, args=(200,))
thr2 = threading.Thread(target=account.down, args=(50,))

thr1.start()
thr2.start()

thr1.join()
thr2.join()
