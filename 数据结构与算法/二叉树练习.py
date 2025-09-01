#以下是二叉树的基础实现与操作的函数名
'''BinaryTree()
 创建一个二叉树实例。
getLeftChild()
 返回当前节点的左子节点所对应的二叉树。
getRightChild()
 返回当前节点的右子节点所对应的二叉树。
setRootVal(val)
 在当前节点中存储参数val中的对象。
getRootVal()
 返回当前节点存储的对象。
insertLeft(val)
 新建一棵二叉树，并将其作为当前节点的左子节点。
insertRight(val)
 新建一棵二叉树，并将其作为当前节点的右子节点。'''
import operator

from pandas.core.groupby.numba_ import validate_udf


#1.列表函数BinaryTree
def BinaryTree(r):
    return [r,[],[]]
#插入左子树
def insertLeft(root,newBranch):
    temp = root.pop(1)
    if len(temp)>1:
        root.insert(1,[newBranch,temp,[]])#如果temp是一个有效的子树，则需要保留
    else:
        root.insert(1,[newBranch,[],[]])
#插入右子树
def insertRight(root,newBranch):
    temp = root.pop(2)
    if len(temp)>1:
        root.insert(2,[newBranch,[],temp])
    else:
        root.insert(2,[newBranch,[],[]])
def getRootVal(root):
    return root[0]
def setRootVal(root,newVal):
    root[0]=newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]

#2.节点与引用
class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
def insertLeft_two(self,newNode):
    if self.leftChild==None:
        self.leftChild=BinaryTree(newNode)
    else:
        temp=BinaryTree(newNode)
        temp.left=self.leftChild#将现有的左子节点 self.leftChild 设置为 temp 的左子节点
        self.leftChild=temp#将 temp 设置为当前节点的左子节点
        #这样，newNode 成为新的左子节点，而原来的左子节点变为新节点的左子节点。相当于将newNode插入到当前子节点和原来的左子节点之间了
def insertRight_two(self,newNode):
    if self.rightChild==None:
        self.rightChild=BinaryTree(newNode)
    else:
        temp=BinaryTree(newNode)
        temp.right=self.rightChild
        self.rightChild=temp
def getRightChild(self):
    return self.rightChild
def getLeftChild(self):
    return self.leftChild
def setRootVal(self,obj):
    self.key=obj#将 obj 赋值给当前节点的 key 属性。self.key 是当前节点的值（或称为键值、根值），obj 是新的值。
def getRootVal(self):
    return self.key
#3.解析数构建器
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
def buildParseTree(fpexp):
    fplist=fpexp.split()
    pStack=Stack()
    eTree=BinaryTree('')
    pStack.push(eTree)
    currentTree=eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')#创建一个新的左子节点
            pStack.push(currentTree)#将当前节点压入栈中
            currentTree=currentTree.getLeftChild()#更新当前节点为新创建的子节点
        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))#eval函数将i转换为数值
            parent=pStack.pop()#从栈中弹出一个父节点
            currentTree=parent#将currentTree更新为该父节点
        elif i in '+-*/':
            currentTree.setRootVal(i)#将i的值设置为当前节点的根值
            currentTree.insertRight()#创建一个新的右子节点
            pStack.push(currentTree)#将当前节点压入栈
            currentTree=currentTree.getRightChild()#更新当前节点为新创建的子节点
        elif i ==')':
            currentTree=pStack.pop()
        else:
            raise ValueError("unkown operator:"+i)
    return eTree
#解析器的递归版本：
def evaluate(parseTree):
    opers={'+':operator.add,'-':operator.sub,
           '*':operator.mul,'/':operator.truediv()}#创建一个字典，将操作符字符串映射到operator模块
    leftC=parseTree.getLeftChild()
    rightC=parseTree.getRightChild()
    #获取当前节点的左子节点和右子节点，如果两个都是None
    if leftC and rightC:#这个if用来判断是否是叶子节点
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
        #evaluate 函数会根据子树的结构返回一个数值：
        #如果子树是叶子节点（没有子节点），返回节点的值（比如 2、3）。
        #如果子树是操作符节点（有子节点），继续递归计算
    else:#这个else就表示如果子树是叶子节点，则返回节点的值
        return parseTree.getRootVal()
#将前序遍历算法实现为外部函数：
def preorder(tree):
    if tree:
        print(tree.getRootVal())#根
        preorder(tree.getLetfChild())#左
        preorder(tree.getRightChild())#右
#将前序遍历算法实现为BinaryTree类的方法：
def preorder_binarytree_version(self):
    print(self.key)
    if self.leftChild:
        self.left.preorder_binarytree_version
    if self.rightChild:
        self.right.preorder_binarytree_version
#中序遍历：
def inorder(tree):
    if tree:
        inorder(tree.getLetfChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
#修改后的中序表达式能够还原完全括号表达式：
def printexp(tree):
    sVal=""
    if tree:
        sVal='('+printexp(tree.getLetfChild())
        sVal=sVal+str(tree.getRootVal())
        sVal=sVal+printexp(tree.getRightChild())+')'
    return sVal
#后序遍历：
def postorder(tree):
    if tree:
        postorder(tree.getRightChild())
        postorder(tree.getLetfChild)
        print(tree.getRootVal())
#后序求值函数：
def postordereval(tree):
       opers = {'+':operator.add, '-':operator.sub,
                '*':operator.mul, '/':operator.truediv}
       res1 = None
       res2 = None
       if tree:
           res1 = postordereval(tree.getLeftChild())
           res2 = postordereval(tree.getRightChild())
           if res1 and res2:
              return opers[tree.getRootVal()](res1, res2)
           else:
              return tree.getRootVal()
#二叉堆的建立和一些用法：（以下均以最小堆为例）
class heap:
    def __init__(self):
        self.heaplist=[0]
        self.currentsize=0
    def percUp(self,i):
        while i // 2>0:
            if self.heaplist[i]<self.heaplist[i//2]:
                temp=self.heaplist[i//2]
                self.heaplist[i//2]=self.heaplist[i]
                self.heaplist[i]=temp
            i=i//2
    #向上堆化
    def insert(self,k):
        self.heaplist.append(k)
        self.currentsize=self.currentsize+1
        self.percUp(self.currentsize)
    #该函数用于向堆中插入元素，同时保证堆的属性不改变
    def minChild(self,i):
        if i*2+1 > self.currentsize:
            return i*2
        else:
            if self.heaplist[i*2]>self.heaplist[i*2+1]:
                return self.heaplist[i*2+1]
            else:
                return self.heaplist[i*2]
    #找到给定节点i的两个子节点中较小的那个子节点的索引
    def percDown(self,i):
        while (i*2)<=self.currentsize:
            minchild=self.minChild(i)
            if self.heaplist[i]>self.heaplist[minchild]:
                temp=self.heaplist[minchild]
                self.heaplist[minchild]=self.heaplist[i]
                self.heaplist[i]=temp
            i=minchild
    #向下堆化，也叫下沉，
    #接下来是删去堆中的最小值（即根节点的值），同时保持堆属性
    def delMin(self):
        delval=self.heaplist[1]
        self.currentsize=self.currentsize-1
        self.heaplist[1]=self.heaplist[self.currentsize]
        self.percDown(1)
        self.heaplist.pop()
        return delval
    #根据元素列表构建堆：
    def buildHeap(self,alist):
        i=len(alist)//2
        self.currentsize=len(alist)
        self.heaplist=[0]+alist[:]
        while i>0:
            self.percDown(i)
            i=i-1
    #利用堆实现排序：，这里是最小堆
    def heapify(self,n,i):#n数组的长度，i当前要调整的节点的索引
        minimum=i
        left=i*2+1
        right=i*2+2

        if i<n and self.heaplist[i]>self.heaplist[left]:
            minimum=left
        if i<n and self.heaplist[i]>self.heaplist[right]:
            minimum=right
        if minimum != i:
            self.heaplist[i],self.heaplist[minimum]=self.heaplist[minimum],self.heaplist[i]
            self.heapify(self,n,minimum)
    def heapSort(self):
        n=len(self.heaplist)
        #构建最小堆：
        for i in range(n//2-1,-1,-1):
            self.heapify(self,n,i)
        for i in range(n,1,-1):
            self.heaplist[i],self.heaplist[1]=self.heaplist[1],self.heaplist[i]
            self.heapify(self,i,1)#这一步可以调整满足最小堆的性质，从堆顶开始，调整其子树
        return self.heaplist
#二叉搜索树的实现：
class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
#已经有了两个类，现在来实现put方法：用于构建二叉搜索树
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size=self.size+1
    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)
#现在实现get方法：在BST中找到key，并取值
    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif key==currentNode.key:
            return currentNode
        elif currentNode < key:
            self._get(key,currentNode.leftChild)
        else:
            self._get(key,currentNode.rightChild)
    def delete(self,key):
        if self.size>1:
            nodeToRemove=self._get(self,key,self.root)
            if nodeToRemove:
                self.size=self.size-1
                self.remove(nodeToRemove)#remove方法在后文
            else:
                raise KeyError("Key not in the tree")
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size=self.size-1
        else:
            raise KeyError("Key not in the tree")
    def remove(self,currentNode):
        #没有子节点的情况
        if currentNode.isleaf():
            if currentNode==currentNode.parent.leftChild:
                currentNode.parent.leftChild=None
            else:
                currentNode.parent.rightChild=None
        #有一个子节点的情况：（未完待续）
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent=currentNode.parent
                    currentNode.parent.leftChild=currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent=currentNode.parent
                    currentNode.parent.rightChild=currentNode.rightChild


        #有一个子节点
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    #需要在TreeNode里面实现__iter__方法，用于BST中进行for循环，综合来看，这个代码是一个中序遍历的生成器
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for element in self.leftChild:
                    yield element
            yield self.key
            if self.hasRightChild():
                for element in self.rightChild:
                    yield element#这个代码先左后右的顺序，所以是进行中序遍历的迭代
'''binarysearchtree类有一个引用，指向作为二叉搜索树根节点的·treenode类'''
#AVL平衡二叉搜索树,注意：叶节点本身的平衡因子是0，但其本身会影响其父节点的平衡因子
class AVL_BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size=self.size+1
    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)
    def updateBalance(self,node):
        if node.balanceFactor>1 or node.balanceFactor<-1:
            self.rebalance(node)#这个是重新平衡的方法
            return
        if node.parent!=None:
            if node.isLeftChild():
                node.parent.balanceFactor +=1
            elif node.isRightChild():
                node.parent.balanceFactor -=1
            if node.parent.balanceFactor !=0:
                self.updateBalance(node.parent)
    #向左旋转的代码实现rotateLeft,向右旋转同理
    def rotateLeft(self,rotRoot):#左旋
        newRoot=rotRoot.rightChild
        rotRoot.rightChild=newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent=rotRoot
        newRoot.parent=rotRoot.parent
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild=newRoot
            else:
                rotRoot.parent.rightChild=newRoot
        newRoot.leftChild=rotRoot
        rotRoot.parent=newRoot
        rotRoot.balanceFactor=rotRoot.balanceFactor+1-min(newRoot.balanceFactor,0)
        newRoot.balanceFactor=newRoot.balanceFactor+1+max(rotRoot.balanceFactor,0)
    def rotateRight(self,rotRoot):#右旋
        newRoot=rotRoot.leftChild
        rotRoot.leftChild=newRoot.rightChild
        if newRoot.rightChild !=None:
            newRoot.rightChild.parent=rotRoot
        newRoot.parent=rotRoot.parent
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild=newRoot#将rotRoot的父节点的左子节点设置为newRoot
            else:
                rotRoot.parent.rightChild=newRoot
        newRoot.rightChild=rotRoot#将rotRoot与newRoot相连
        rotRoot.parent=newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 + max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 - min(rotRoot.balanceFactor, 0)
    #在考虑写rebalance时，要综合考虑各种旋转的情形
    def rebalance(self,node):
        if node.balanceFactor<0:#此时是右重，需要左旋
            if node.rightChild.balanceFzctor>0:#右子节点左重，需要先右旋
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor>0:#此时是左重，需要右旋
            if node.leftChild.balanceFactor<0:#左子节点右重，需要其先左旋
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)