#1.Node类
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newdata):
        self.next=newdata
#2.Unorderedlist类(存疑)
class Unorderedlist:
    def __init__(self):
        self.head=None
        self.size=0
    def append(self, item):
        """在链表尾部追加新元素"""
        new_node = Node(item)
        if self.head is None:  # 空链表
            self.head = new_node
        else:
            current = self.head
                # 遍历到最后一个节点（current.next 为 None 时停止）
            while current.next is not None:
                current = current.next
            current.next = new_node  # 将新节点链接到末尾
        self.size += 1  # 更新长度
    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>=self.size:
            self.append(item)
        else:
            new_node=Node(item)
            current=self.head
            #遍历到插入为止的前驱节点
            for _ in range(pos-1):
                current=current.next
            #插入新节点
            new_node.next=current.next# 新节点的 next 指向当前节点的下一个节点
            current.next=new_node# 当前节点的 next 指向新节点
            self.size+=1
    def index(self,item):
        current=self.head
        index=0
        while current is not None:
            if current.data==item:
                return index
            current=current.next
            index+=1
        raise ValueError(f"{item} not in list")
    def pop(self,pos=-1):
        if self.size==0:

            raise IndexError("pop from empty list")
        #处理默认参数pos=-1
        if pos==-1:
            pos=self.size-1
        #验证索引范围
        if pos<0 or pos>=self.size:
            raise IndexError("pop index out  of range")
        #删除头节点：
        if pos==0:
            data=self.head.data
            self.head= self.head.next
            self.size-=1
            return data
        #处理中间或尾部节点:
        current=self.head
        for _ in range(pos-1):#遍历找到前驱节点
            current=current.next
        data=current.next.data
        current.next=current.next.next
        self.size -=1
        return data

#前面基础还需要练习，现在从遍历链表的方法开始
#length方法获取链表长度
def length(self):
    current=self.head
    count=0
    while current != None:
        count=count+1
        current = current.getNext()
    return count
#search方法
def search(self,item):
    current=self.head()
    found = False
    while current != None and not found:
        if current.getData()==item:
            found =True
        else:
            current=current.getNext()
    return found
#remove方法
def remove(self,item):
    current = self.head
    previous = None
    found = False
    while not found:
        if current.getData()==item:
            found = True
        else:previous=current.getNext()

    if previous == None:
       self.head=current.getNext()
    else:
        previous.setNext()(current.getNext())

