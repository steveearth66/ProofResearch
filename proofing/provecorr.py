from testprompt import getnum, intsqrt
N=getnum()
S = N
for i in range(S): S += 2*i
while intsqrt(S) != N: print("loops")
print("success")