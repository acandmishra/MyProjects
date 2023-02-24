class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def PreOrder(self):
        print(self.data)
        if self.left != None:
            self.left.PreOrder()
        if self.right != None:
            self.right.PreOrder()

    def PostOrder(self):
        if self.left != None:
            self.left.PostOrder()
        if self.right != None:
            self.right.PostOrder()
        print(self.data)

    def InOrder(self):
        if self.left != None:
            self.left.InOrder()
        print(self.data)
        if self.right != None:
            self.right.InOrder()

    def Insert(self,data):
        New=Node(data)
        while(True):
            if(data<self.data):
                if self.left==None:
                    self.left=New
                    break
                elif data>self.left.data:
                    New.left=self.left
                    self.left=New
                    break
                else:
                    self=self.left
            elif(data>self.data):
                if self.right==None:
                    self.right=New
                    break
                elif data<self.right.data:
                    New.right=self.right
                    self.right=New
                    break
                else:
                    self=self.right
            else:
                print("duplicate data")
                exit(0)
        print("insertion done")
        


A=Node(50)
B=Node(30)
C=Node(70)
D=Node(20)
E=Node(40)
F=Node(60)
G=Node(80)
A.left=B
A.right=C
B.left=D
B.right=E
C.left=F
C.right=G

# A.PreOrder()
# print("-------")
# A.PostOrder()
# print("-------")
# A.InOrder()
A.PostOrder()
A.Insert(10)
A.PostOrder()
A.Insert(15)
A.PostOrder()
