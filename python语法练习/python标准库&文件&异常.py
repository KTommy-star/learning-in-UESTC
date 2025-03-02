#python标准库基础练习演示
'''from random import randint
class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        result=randint(1,self.sides)
        print(f"抛出了：{result}")
        return result

six_sides_die=Die()

for i in range(10):
    six_sides_die.roll_die()'''

#文件
'''filename = 'pi_digit.txt'
with open(filename) as file_object:
    #read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行，可以调用print()时使用rstrip()
    contents = file_object.read()
print(contents)
#逐行读取
filename = 'pi_digit.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
#使用文件的内容
filename = 'pi_digit.txt'
with open(filename) as file_object:
    #.readlines()读取文件中的每一行信息并将其存储在一个列表中
    lines = file_object.readlines()
pi_string=''
for line in lines:
    #使用strip而非rstrip是删除指向的字符串包含原来位于每行左边的空格
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))'''
#写入文件
'''filename = 'pi_digit.txt'
with open(filename,'a') as file_object:
    file_object.write("I love Ms.Optimist.\n")
    file_object.write("I'm learning Python now.\n")'''
#异常的基础练习1
print("Give me two numbers to be divides.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nenter first number:")
    if first_num == 'q':
        break
    second_num = input("\nenter second number:")
    if second_num == 'q':
        break
    try:
        answer = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print("分母不能有为0")
        break
    else:
        print(answer)
        break
#异常的基础练习2（计算文件中单词数的函数）
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
          contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        '''pass'''#使用pass可以静默失败，即发生错误也不提示，继续运行其他代码
    else:
      # 计算该文件大致包含多少个单词。
      # split()以空格将字符串拆分成多个部分，并将这些部分都存储在一个列表中
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")