#定义队列Queue:FIFO
class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]
    #队列尾部添加元素
    def enqueue(self,item):
        self.items.insert(0,item)
    #队列头部去除元素
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
#热土豆游戏
#调用hotpotato函数需要输入一个列表和传递的数字 
from pythonds.basic import Queue
def hotpotato(namelist,num):
    simqueue=Queue()
    #根据名单加入元素填充空队列
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        #将队列中的元素从一个端移除并添加到另一个端
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    #循环结束后队列只剩一个元素，就是留下来的那个
    return simqueue.dequeue()
#定义双端队列：Deque:  eg.写回文检测器
class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
