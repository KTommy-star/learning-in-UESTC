#进制转换器
'''def toStr(n,base):
    stringcover="0123456789ABCDEF"
    if n < base:
        return stringcover[n]
    else:
        return toStr(n//base,base)+stringcover[n%base]
print(toStr(8,2))
#借助栈的思想，改进这个代码，浅栈,该函数压入栈
from pythonds.basic import Stack
def toStr_improved(n,base):
    rstack=Stack()
    stringcover = "0123456789ABCDEF"
    if n < base:
        rstack.push(stringcover[n])
    else:
        rstack.push(stringcover[n%base])
        toStr_improved(n//base,base)'''
from ply.yacc import resultlimit

#递归可视化1
'''from turtle import *
myTurtle=Turtle()
myWin=myTurtle.getscreen()

def drawspiral(myTurtle,Line0.len):
    if Linelen >0:
        myTurtle.forward(Linelen)
        myTurtle.right(60)
        drawspiral(myTurtle,Linelen-5)
drawspiral(myTurtle,200)
myWin.exitonclick()'''
#递归可视化2
'''from turtle import *
def tree(branchlen,t):
    if branchlen>5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen-15,t)
        t.left(40)
        tree(branchlen-10,t)
        t.right(20)
        t.backward(branchlen)
t=Turtle()
myWin=t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110,t)
myWin.exitonclick()'''
#找出数组子序列求和最大值
def find_max_sum(nums):
    if not nums:
        return None
    current_max=max_sum=nums[0]
    for num in nums[1:]:
        current_max=max(num,num+current_max)
        max_sum=max(current_max,max_sum)
    return max_sum
num1=[1,-3,2,-9,4,-1,5,7,-10]
print(find_max_sum(num1))
#递归计算数的阶乘
def calculate_jiecheng(n):
    if n==0:
        return 1
    return n * calculate_jiecheng(n-1)

result=calculate_jiecheng(4)
print(result)
#递归反转列表
def reserved_list(lst):
    if len(lst) <=1:
        return lst
    #递归反转除第一个元素之外的子列表，并将第一个元素添加到末尾
    return reserved_list(lst[1:])+[lst[0]]
test_lisy=[1,2,3,4,5]
result=reserved_list(test_lisy)
print(result)

