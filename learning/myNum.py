##from myDriver import g

class MyNum():
    def __init__(self, num):
        self.value= num
    def inc(self):
        self.value+=11

x=MyNum(42) #intended to be global
