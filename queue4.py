from collections import deque 
import threading 
import time

class Queue:
    def __init__(self):
        self.deque=deque() 

    def enqueue(self,data):
        self.deque.appendleft(data)

    def dequeue(self):
        return self.deque.pop()

    def size(self):
        return len(self.deque)

    def is_empty(self):
        return len(self.deque)==0


orders=["Pizza","Samosa","Pasta","Chicken Wings","Burger"]


qu=Queue()

def placeOrder(orders):
    for order in orders:
        print(f"The placed order is: {order.upper()}")
        qu.enqueue(order)
        time.sleep(0.5)


def serveOrder():
    time.sleep(1)
    while True:
        try:
            print(f"Serving order: {qu.dequeue().upper()}")
            time.sleep(2)
        except Exception as e:
            print("All orders are served, Thank you.")
            break


# t1=threading.Thread(target=placeOrder,args=(orders,))
# t2=threading.Thread(target=serveOrder)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

for i in range(1,11):
    print(bin(i).replace("0b",""))



    
    