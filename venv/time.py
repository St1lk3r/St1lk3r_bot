import threading
import time



def f():
    print("ЫП ап ып да")
    myThread.run()


if __name__ == '__main__':
    myThread = threading.Timer(1, f)
    myThread.start()

a = {"RUB" : {"15m" : 450165.49, "last" : 450165.49, "buy" : 450165.49, "sell" : 450165.49, "symbol" : "RUB"},
     "USD": {"15m": 6709.57, "last": 6709.57, "buy": 6709.57, "sell": 6709.57, "symbol": "$"}}

print(a)


