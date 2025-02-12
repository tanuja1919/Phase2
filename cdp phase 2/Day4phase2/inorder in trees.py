class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class trees:
    def __init__(self):
        self.root=None
    def insert(self,value):
        newnode=node(value)
        if not self.root:
            self.root=newnode
        else:
            curr=self.root
            while True:
                if curr.data>value:
                    if curr.left==None:
                        curr.left=newnode
                        break
                    else:
                        curr=curr.left
                else:
                    if curr.right==None:
                        curr.right=newnode
                        break
                    else:
                        curr=curr.right
    def inorder(self):
        self.helper(self.root)
    def helper(self,root):
        if root:
            self.helper(root.left)
            print(root.data)
            self.helper(root.right)
t=trees()
t.insert(5)
t.insert(3)
t.insert(4)
t.insert(8)
t.insert(7)
t.insert(6)
t.insert(2)
t.inorder()
