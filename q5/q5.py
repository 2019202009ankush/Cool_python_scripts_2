
class node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

l=[]

class BST(object):

    def __init__(self):
        self.root=None
        self.co=0

    def _insertL(self,arr,root,i, n):
        if i < n:
            if arr[i] != -1 :
                self.co = self.co + 1
                # print("i=",i,n)
                temp = node(arr[i])
                root = temp
                root.left = self._insertL(arr, root.left,2*i+1,n)
                root.right = self._insertL(arr, root.right,2*i+2,n)
            else:
                self.co+=1
        return root

    def insertL(self,arr,i,n):
        self.root=self._insertL(arr,self.root,i,n)





    def preorder(self,root):
        if root ==None :
            return
        else:

            print(root.data,end="--")
            self.preorder(root.left)
            self.preorder(root.right)
    def printLeft(self,root):
        if root:
            if root.left:
                l.append(root.data)
                self.printLeft(root.left)
            elif root.right:
                l.append(root.data)
                self.printLeft(root.right)
    def printRight(self,root):
        if root:
            if root.right:
                self.printRight(root.right)
                l.append(root.data)
            elif root.left:
                self.printRight(root.left)
                l.append(root.data)
    def printLeaves(self,root):
        if root:
            self.printLeaves(root.left)
            if not root.left and not root.right:
                l.append (root.data)
            self.printLeaves(root.right)

    def boundary(self,root):
        self.printLeft(root)
        self.printLeaves(root)
        self.printRight(root.right)

import inflect

n=input()
#n = '''40 20 60 10 30 50 70 -1 5 -1 -1 -1 55 -1 -1 -1 -1 -1 45 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1'''
v=n.split(" ")
arr=[]
for i in v:
    temp=int(i)
    arr.append(temp)
bst=BST()
# print(len(arr))
bst.insertL(arr,0,len(arr))
#print(bst.preorder(bst.root))
bst.boundary(bst.root)
l.append(l[0])
print("Total Amount : ",inflect.engine().number_to_words(sum(l)))
print('Order :',','.join([inflect.engine().number_to_words(i).capitalize() for i in l]))