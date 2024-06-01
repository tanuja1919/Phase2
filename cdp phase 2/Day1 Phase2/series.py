n=10
a=0
b=1
c=0
print(a)
print(b)
print(c)
for i in range(4,n+1):
    d=a+b+c
    print(d)
    a=b
    b=c
    c=d
    
