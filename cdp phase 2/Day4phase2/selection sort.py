l=[1,3,5,6,7,9]
for i in range(len(l)-1):
    m=i
    for j in range(i+1,len(l)):
        if l[j]<l[m]:
            m=j
    l[i],l[m]=l[m],l[i]
print(l)
