'''
print("Hello, Python!")
print("man!!!")
print("mamba out!")
print("此刻，寂灭之时！")
import keyword
print(keyword.kwlist)#打印所有的保留字
print((len(keyword.kwlist))) #获取保留字的个数
my_name='kjx'
print('my_name的数据类型是：',type(my_name))#type是用于测量变量的数据类型
num=9987 # 默认十进制
num2=0b1010110 # 二进制
num3=0o765 # 八进制
num4=0x87ABF # 十六进制
print(num)
print(num2)
print(num3)
print(num4)
x = 123+456j#含j表示虚数
print('x的实数部分是：',x.real)#.real是表示实数部分
print('x的虚数部分是；',x.imag)#.imag是表示虚数部分
s='HELLOWORLD'
#以下为根据位置打印出相应字符
print(s[2],s[9])
print('北京欢迎你'[4])
print(s[2:7])
m='2024年'
n='重庆欢迎你'
print(m+n)
print(7*m)#利用乘法打印多次
# print('重庆' in n)#in用于检查引号里的字符串是否属于原定义好的变量
w='3.14+2'
i=eval(w) # 去掉w这个字符串中左右的引号，并执行加法运算，这是·eval函数的应用
print(round(i,2),type(i))#round表示保留几位小数
print(round(2.35+3.16,2))#加法，结果保留两位小数
age=eval(input('请输入你的年龄：'))
print(age,type(age))
beloved=(input('请输入你的爱人的名字：'))
print('您爱人的名字是：' +beloved,type(beloved))#引用时注意使用 + 作为连接符
print(2 ** 50)#**表示乘方
x = 300
y = 10.0
x /= y
print(x,type(x))
z = 69
z %=4 # 取余
print(z)
print('98大于90吗？',98>90)
print('98小于90吗？',98<90)
print('98不等于90吗？',98!=90)
print('-'*50)
#逻辑比较符号
print(8>7 and 6>5)
print(8<7 or 6>5)
print(8<7 and 6<5)
'''
from random import random

#以上是以前的东西
'''print(12&8)#按位与计算
print(12|8)#按位或计算
print(12^8)#按位异或计算
print(~128)#按取反计算
print('左移位：', 2<<2)#表示2向左移动两位 2*2*2
print('右移位（左侧最高位是啥就补啥）:',8>>2)#向右移动两位,8//2,4//2
a,b,c,d='room'#字符串分解赋值

#if的第一种
number=eval(input('请输入你的6位中奖号码'))
if number==987654:
    print('恭喜中奖！')
if number!= 987654:
    print('很遗憾未中奖')
print('---------判断一个字符串是否是空字符串----------')
x=input('请输入一个字符串：')
if not x:
    print('x是一个空字符串')
if x:
    print('x是一个非空字符串')

#if的第二种
num = eval(input("输入你的彩票号码："))
#第一种简化书写
result='win'if num == 123456 else 'false'
print(result)
#第二种简化书写
print('win'if num == 123456 else 'false')

#多分支结构
score=eval(input("请输入你的成绩："))
if score > 100 or score<0:
    print('成绩有误！')
elif 0<= score < 60:
    print('没有及格偶！！！')
elif 60< score <=80:
    print('将将就就')
else:
    print('很优秀嘛孩子')

#if的嵌套使用
#使用and连接多个条件判断时，只有满足多个条件，才能继续正常执行
#使用or连接多个条件判断时，只要满足某一个条件，就能继续正常执行

#python3.1.1的新东西：模式匹配 match-case结构'''

#for循环遍历
for i in range(1,11):#注意是包含1不包含11
    if i%2==0:
        print(i,'是偶数')
for j in 'hello':
    print(j)
s=0
for w in range(1,1000):
    s+=w
print('和为',s)
print('----------------------------------------')
#寻找100--1000的水仙花数
for i in range(100,1001):
    a=i%10
    b=i//10%10
    c=i//100
    if i==a**3+b**3+c**3:
        print(i,'是水仙花数')
#for-else循环(for的扩展)
#注意：else要在循环正常结束后才执行
s=0
for i in range(1,77):
    s+=i
else:
    print('1-77和为：',s)

#while无限循环：初始化变量、条件判断、语句块、改变变量
s=0
i=1
while i<=300:
    s+=i
    i+=1
print('1-300累加和为:',s)
#while-else循环(while的扩展)
#注意：else要在循环正常结束后才执行

#模拟用户登录输入账号和密码
i=0#初始化变量
while i < 3:
    user_name=input('请输入您的用户名：')
    pwd=input('请输入您的密码')
    if user_name=='kjx' and pwd== '88888888':
        print('正在进入系统，请稍后...')
        break#用于结束while循环
    else:
        if i < 2:
            print('账号或密码输入错误，你还有',2-i,'次机会')
        i+=1

if i==3:
    print('sb三次都错了！你肯定是贼！滚！！')

##while的嵌套
#1.直角三角形
for i in range (1,6):#有5行
    for j in range (1,i+1):#每一行打几个*
        print('*',end='')
    print()
#2.倒着的直角三角形
for i in range (1,6):#有5行
    for j in range (1,6-i):#每一行打几个*
        print('*',end='')
    print()
#3.等腰三角形
print('-----------------------------')
for i in range(1,6):
    for j in range (1,6-i):
        print(" ", end='')
    for k in range (1,i*2):
        print('*',end='')
    print()
print('---------------------------')
#菱形（只能是奇数行）
row=eval(input('请输入菱形的行数'))
while row%2==0:
    print('请重新输入：')
    row = eval(input('请输入菱形的行数'))
#上半部分
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ', end='')#打印倒三角形空格
    for k in range(1,i*2):
        print('*',end='')#打印等腰三角形
    print()
#下半部分
bottom_row=row//2
for i in range (1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')#打印正的直角三角形
    for k in range(1,2*bottom_row-2*i+2):#根据算法，写出打印*的顺序内容
        print('*', end='')
    print()

#空心菱形
print('-----------------------------')
row=eval(input('请输入菱形的行数'))
while row%2==0:
    print('请重新输入：')
    row = eval(input('请输入菱形的行数'))
#上半部分
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ', end='')#打印倒三角形空格
    for k in range(1,i*2):
        if k == 1 or k == i*2-1:
            print('*',end='')
        else:
            print(' ',end='')#通过判断，只在首尾位置打印*
    print()

#下半部分
bottom_row=row//2
for i in range (1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):
        if k == 1 or k == 2*bottom_row-2*i+1:
            print('*',end='')
        else:
            print(' ',end='')#通过判断，只在首尾位置打印*
    print()
#continue的使用（累加求和问题升级，只求偶数和）
for i in range (1,101):
    if i %2 != 0:
        continue
    s+=i
print('1~100之间的偶数和为：',s)

#列表的遍历：
lst = ['hello','world','python','genshin']
#第一种
for item in lst:
    print(item)
#第二种
for i in range(0,len(lst)):
    print(i,'-->',lst[i])
#第三种
for index,item in enumerate(lst,start=1):#start=1可以不写
    print(index,item)
#列表的排序
lst=[1,3,6,9,42,674,3979,4546,9749,12132]
lst.sort(reverse=True)
print('降序',lst)
lst1=['banana','apple','Cat','dog']
lst1.sort(key=str.lower)#全部化为小写字母再来排序
print(lst1)
#用python写Genshin Impact especially for 小金羽
print('草拟吗')
lst=[i for i in range(100) if i%2==0]
print(lst)
#创建二维列表并遍历
lst=[
    ['城市','单价','面积'],
    ['重庆',1,140],
    ['北京',7,70],
    ['上海',7,83],
]
for row in lst:#行
    for item in row:#列
        print(item,end='\t')
    print()#换行
'''a = 1
b = 10
lst=[random.randint(a,b) for _ in range (10)]
print(lst)'''
#元组的一些注意操作
t=(i for i in range(1,4))#定义了一个元组生成式
print(t)#此时会打印出生成器 <generator object <genexpr> at 0x000002B0B5C4D900>
'''t=tuple(t)
print(t)#此时会打印出元组里面的元素，即123'''
print(t.__next__())
print(t.__next__())
print(t.__next__())#这三行使用next操作，让元组生成式在未转换成元组是能够打印出其中的元素
#使用zip函数创建字典
lst1={10,20,30,40}
lst2={'Amy','Bob','Cendy','David'}
zipoly=zip(lst1,lst2)
print(zipoly)#<zip object at 0x000002B0B5F88A40>
#print(list(zipoly))#[(40, 'David'), (10, 'Cendy'), (20, 'Bob'), (30, 'Amy')]转换为列表进行打印
d=dict(zipoly)
print(d)#{40: 'Amy', 10: 'Cendy', 20: 'David', 30: 'Bob'}转换为字典类型
c=dict(bob=10,cat=20)
print(c)#{'bob': 10, 'cat': 20}