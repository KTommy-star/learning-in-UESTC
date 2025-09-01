#二分搜索(适用于有序列表)
def binary_search(list,item):
    first = 0
    last = len(list)-1
    found = False
    while first<=last and not found:
        midpoint=(first+last)//2
        if midpoint == item:
            found = True
        else:
            if item<list[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    return found
lst=[1,2,3,4,5,6,7]
item1=8
result=binary_search(lst,item1)
print(result)
#二分搜索的递归版本(适用于有序列表)
def binary_search_recursion(alist,item):
    if len(alist)==0:
        return False
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binary_search_recursion(alist[:midpoint],item)
            else:
                return binary_search_recursion(alist[midpoint+1:],item)
lst=[1,2,3,4,5,6,7]
item1=4
result=binary_search_recursion(lst,item1)
print(result)