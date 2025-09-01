#栈的基础结构：
class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
#十进制转换为任意进制
from pythonds.basic import Stack
def divideby2(decNumber,base):
    digits="0123456789ABCDEF"
    remstack=Stack()

    while decNumber >0:
        rem=decNumber%base
        remstack.push(rem)
        decNumber=decNumber // base
    binstring=''
    while not remstack.isEmpty():
        binstring=binstring+digits[remstack.pop()]
    return binstring

print(divideby2(16579,16))
#中序表达式转后序表达式
from pythonds.basic import Stack
import string

def infixToPostfix(infixexpr):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1

    opstack=Stack()
    postfixList=[]
    tokenlist=infixexpr.split()

    for token in tokenlist:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token =='(':
            opstack.push(token)
        elif token ==')':
            toptoken=opstack.pop()
            #如果 token 是右括号 )，则需要将栈中从最近一个左括号 ( 到栈顶的所有操作符弹出，并添加到 postfixList 中。
            while toptoken != '(':
                postfixList.append(toptoken)
                toptoken=opstack.pop()
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()]>=prec[token]):
                postfixList.append(opstack.pop())
            opstack.push(token)
            while not opstack.isEmpty():
                postfixList.append(opstack.pop())
    return " ".join(postfixList)#join方法连接字符
#使用栈在十进制转二进制
def shi_er(shijinzhishu):
    stack=Stack()
    while shijinzhishu>0:
        yushu=shijinzhishu%2
        stack.push(yushu)
        shijinzhishu=shijinzhishu//2
    erjinzhi=""
    #现在将栈中的元素弹出
    while not stack.isEmpty():
        erjinzhi += str(stack.pop())
    return erjinzhi
shijinzhishu=17
erjinzhishu=shi_er(shijinzhishu)
print(f"十进制数{shijinzhishu}，二进制数{erjinzhishu}")

