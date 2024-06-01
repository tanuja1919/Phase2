class node:
    def __init__(self,data=0):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatbeg(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
    def insertatend(self,value):
        newnode=node(value)
        if not self.head:
            self.head=newnode
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def delatbeg(self):
        if not self.head:
            return
        else:
            self.head=self.head.next
    def delatend(self):
        if not self.head:
            return
        if self.head.next==None:
            self.head==None
        else:
             curr=self.head
             while(curr.next.next!=None):
                 curr=curr.next
             curr.next=None
                        
a=linkedlist()
a.insertatbeg(1)
a.insertatbeg(2)
a.insertatbeg(3)
a.insertatbeg(4)
a.insertatend(5)
a.delatbeg()
a.delatend()
a.printlist()





'''print(a.head.data)
print(a.head.next.data)
print(a.head.next.next.data)
print(a.head.next.next.next.data)'''
        
