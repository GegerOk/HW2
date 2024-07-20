import queue
import threading
import time
import random

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe(queue.Queue):
    def __init__(self, tables):
        super().__init__()
        self.tables = tables

    def customer_arrival(self):
        while True:
            time.sleep(1)
            new_customer = Customer()
            self.put(new_customer)

    def serve_customer(self):
            x = 0
            while True:
                x += 1
                customer = self.get()
                for table in self.tables:
                    if not table.is_busy:
                        table.is_busy = True
                        print(f"Посетитель номер {x} занял стол {table.number}")
                        time.sleep(5)
                        table.is_busy = False
                        print(f"Посетитель номер {x} покинул стол {table.number}")
                self.put(customer)

class Customer(threading.Thread):
    def req(self):
        cafe = Cafe([Table(i) for i in range(1, 5)])
        t1 = threading.Thread(target=cafe.customer_arrival)
        t1.start()
        t2 = threading.Thread(target=cafe.serve_customer)
        t2.start()
        t1.join()
        t2.join()

customer = Customer()
customer.req()