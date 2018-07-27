from math import sqrt, floor
def getnum():
    err = "please enter a nonnegative integer"
    while True:
        try:
            N=int(input("enter int: "))
        except ValueError:
            print(err)
            continue
        if N<0:
            print(err)
            continue
        else: return N

def intsqrt(x):
    return floor(sqrt(x)+.5)
