#冒泡排序
from turtledemo.sorting_animate import partition

from mpmath.calculus.differentiation import dpoly


def bubbleSort(alist):
    #len(alist)-1为起始点，0为结束点，-1为步长，在此处代表递减遍历
    for passum in range(len(alist)-1,0,-1):
        for i in range(passum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
#短冒泡：只需要遍历几次列表，节省性能
def shortBubbleShort(alist):
    '''算法分析：进入while循环，exchange定义为False，先对passum进行for的依次循环，
    假设全都满足alist[i]<=alist[i+1]，那么exchange则一直为False，则外层循环只进行一次，
    其他情况以此类推，这就减少了遍历次数，省下了很多性能'''
    exchange=True
    passum=len(alist)-1
    while passum>0 and exchange:
        exchange=False
        for i in range(passum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist=alist[i+1]
                alist[i+1]=temp
        passum=passum-1
#选择排序：
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax=location

        temp=alist[fillslot]
        alist[fillslot]=alist[positionOfMax]
        alist[positionOfMax]=temp
#插入排序：
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue=alist[index]
        position=index
        '''当遇到比他大的时候，大的数右移，可以理解代码为相邻交换，大的向右走'''
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue
#希尔排序：
def shellSort(alist):
    sublistcount=len(alist)//2
    while sublistcount>0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        print("After increments of size",sublistcount,"The list is",alist)
        sublistcount=sublistcount//2
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue=alist[i]
        position=i
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position=position-gap
        alist[position]=currentvalue
#归并排序（重点是拆分和归并），是一个递归用法，所展示的mergeSort函数需要额外的空间来存储切片操作得到的两半部分
def mergeSort(alist):
      print("Splitting ", alist)
      if len(alist) > 1:
           mid = len(alist) // 2
           lefthalf = alist[:mid]
           righthalf = alist[mid:]

           mergeSort(lefthalf)
           mergeSort(righthalf)
           #以下负责将两个小的有序列表归并为一个大的有序列表
           i = 0
           j = 0
           k = 0
           while i < len(lefthalf) and j < len(righthalf):
               if lefthalf[i] < righthalf[j]:
                   alist[k] = lefthalf[i]
                   i = i + 1
               else:
                   alist[k] = righthalf[j]
                   j = j + 1
               k = k + 1

           while i < len(lefthalf):
               alist[k] = lefthalf[i]
               i = i + 1
               k = k + 1

           while j < len(righthalf):
               alist[k] = righthalf[j]
               j = j + 1
               k = k + 1
      print("Merging ", alist)
#快速排序：
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
    if first>last:
        splitpoint=partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
    pivotvalue=alist[first]
    leftmark=first+1
    rightmark=last
    done = False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
            leftmark=leftmark+1
        while alist[rightmark]>=pivotvalue and rightmark>=leftmark:
            rightmark=rightmark-1
        if rightmark<leftmark:
            done = True
        else:
            temp=alist[leftmark]
            alist[leftmark]=alist[rightmark]
            alist[rightmark]=temp
    temp=alist[first]
    alist[first]=alist[rightmark]
    alist[rightmark]=temp
    return rightmark

lst_example=[1,65,93,79,65,96,88,46]
insertionSort(lst_example)
print(lst_example)