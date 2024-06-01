#list using...


'''l=[1,2,3,4,5,0,8,9,4]
m=0
for i in range(len(l)):
    print(l[i])'''

'''
l=[1,2,3,4,5,0,8,9,4]
m=0
for i in l:
    if i>m:
        m=i
    print(m)'''


'''l=[-1,-2,-3]
m=l[0]
for i in l:
    if i>m:
        m=i
print(m)'''



l=[-1,-2,-3]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
       print(m)  
    
