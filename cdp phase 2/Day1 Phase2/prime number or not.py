#prime number or not





'''n=7
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")'''








import math as m
n=21
for i in range(2,int(m.sqrt(21))):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")





