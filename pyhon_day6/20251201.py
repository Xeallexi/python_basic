#函数
#组织好的，可重复使用，用来实现特定功能的代码段 
"""
length = len("xeallex")
print(length)

data = str(input("输入字符串"))
def my_len(data):
    count = 0
    for i in data:
        count += 1
        print(f"{data}该字符串有{count}个字符")
    return count
my_len(data)
"""
#函数的基础定义 定义完成后需要调用
# def函数名(): 
#    函数体
"""
def hi():
    print("hi")
hi()
"""

#传入参数的使用
"""
def add(x,y): #形参 参数数量不限制
    result = x + y
    print(f"{x}+{y}的结果是：{result}")
add(5,6) #实参
"""
#练习
"""
temp = int(input("请输入体温:"))
def judge(temp):
    if temp < 37.5:
        print("体温正常")
    else:
        print("发烧")
judge(temp)
"""

#返回值 通过return，向调用者返回数据
"""
def add(a,b):
    result = a + b
    return result
r = add(3,4)
f = add(3,5)
print(r)
print(f)
def add(x,y): 
    result = x + y
    print(f"{x}+{y}的结果是：{result}")
add(5,6)
"""
#None
#无返回值时返回none
"""
def hi():
    print("hi")
result = hi()
print(f"{result}",type(result))
#none = false 和if联动
def check_age(age):
    if age > 18:
        return "s"
    else:
        return None
result = check_age(12)
if not None:
    print("未成年")
"""
#用于声明无初始内容的变量 name = None

#定义函数
#在def后加入"""
#  """

def add(x,y):
    """
    :x
    :y
    """
    result = x + y
    print(f"两数相加的结果是：{result}")
    return result

#函数的嵌套
"""
def fun_b():
    print("==2==")
def fun_a():
    print("==1==")
    fun_b()
    print("==3==")
fun_a()
"""
#变量的作用范围 在函数里的变量作用域仅存于函数内
"""
def testa():
    num = 100
    print(num)
testa()
#print(num) num未定义
"""
#globoal 将局部变量转为全局变量
"""
num = 100
def testa():
    print(num)
def testb():
    global num
    num = 200
    print(num)
testa()
testb()
print(num)
"""

#return 可以有多个返回值 比如return 1,2 安顺序对应多个变量
"""
def test_return():
    return 1,2
x,y = test_return()
print(x)
print(y)
"""

#函数的多种传参形式
#【1】位置参数
#【2】关键字参数 键=值
def user_info(name,age,gender):
    print(f"你的名字是：{name},年龄是：{age}，性别是：{gender}")
user_info(name = "xea",age = 21,gender="男")
user_info('xea',age=21,gender="女")
#【3】缺省参数 可以通过在函数直接给一个默认值 通过改变进行覆盖 
# 默认值只能从后往前覆盖 不能直接改第一个为默认值
def user_info(name,age=21,gender = "男"):
    print(f"你的名字是：{name},年龄是：{age}，性别是：{gender}")
user_info(name = "xea")
user_info('xea',age=22,gender="女")
#【4】不定长参数以后学

#函数作为参数传递 代码的逻辑传递
"""
def test(compute):
    result  = compute(1,2)
    print(result)
def compute(x,y):
    return x  + y
test(compute)
"""
#匿名函数 lamdba 只能临时用一次，而且只能写一行
#lambda x,y : x+y
def test(compute):
    result  = compute(1,2)
    print(result)
test(lambda x,y:x+y)

