##def f(x):
##    return x+1

from myDriver import fg
from myNum import MyNum, x

w1 = MyNum(0)
fg(w1)
print("after myfun, w="+str(w1.value))
print("after myfun, x="+str(x.value))