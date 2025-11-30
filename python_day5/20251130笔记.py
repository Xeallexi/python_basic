#2025.11.30 day5

#for的学习
#for循环 与while不同，可以自行控制循环条件
"""
name = "xeallex"
for x  in name: #将name的内容去处赋予x临时变量
    print(x)
"""
#数一数句子中的字母数字
"""
name = "xeaxxxxllex"
a = 0
for x in name:
    if x == "x":
        a += 1
print(f"{name}中共含有{a}个字母x")
"""
#range语句
#1.range(num) 从零开始到num结束，不包含num
#for x in range(10):
 #   print(x)

#2.range(num1,num1) num1开始到num2结束，不包含num2
#for x in range(7,10):
 #   print(x)

#3.range(num1,num2,step) num1到num2，step为数字间的步长
#for x in range(1,10,2):
 #   print(x)
#for x in range(19):
 #   print("i luv u")

"""
#输入数字找偶数
num = int(input("请输入数字"))
a = 0
for x in range(1,num+1):
    if x%2 == 0:
        a += 1
print(f"1到{num}范围内，有{a}个偶数")
"""

#for循环临时变量作用域 只作用于for中，但非强制限定，可以先定义变量
"""
i = 0
for i in range(5):
    print(i)
print(i)
"""

#for的嵌套
"""
i = 1
while i<=10:
    print(f"第{i}天")
    for j in range(1,11):
        print(f"尝试{j}次")
    i += 1
print(f"第{i-1}天成功")
"""
#continue和break continue:跳过本次循环 break:终结所有循环

#for i in range(1,11):
 #   print(i)
  #  if i == 4:
   #     continue
"""
for i in range(1,6):
    print("x")
    for j in range(1,6):
        print("xx")
        break #该break只是在本次循环废除，下一次还是要进这个循环
        print("xxxx")
    print("xxxx")
"""




#列表的学习
#数据容器 可以容纳任意类型数据
#name_list = ['a','b',123,True]
#print(name_list)

#列表
# []作为标识 list()空列表 ['a','b']
"""
my_list = [[1,2,3],[4,5,6]]
for sub_list in my_list:
    for num in sub_list:
        print(num,end='')
    print()
    """
#下标索引 从0开始 反向索引 从-1往前数
#name_list = ['a',1,2,3]
#print(name_list[0])
#print(name_list[-4])
#下标索引嵌套的应用
#sub_list = [[1,2,3],[4,5,6]]
#print(sub_list[0][2]) #取第一个列表里的第三个数字




#列表的方法
# 【1】
#index用于查找指定元素列表的下标
mylist = ["a","b","c"]
#index = mylist.index("a")
#print(f"在位置中的下标是：{index}")
#元素不存在会报错
#index = mylist.index("h")
#print(f"在位置中的下标是：{index}")

# 【2】
#修改特定位置的元素值 列表[下标] = ？
#mylist[0] = "d"
#print(mylist)

#【3】
#通过.insert插入指定元素
#mylist.insert(1,"f") 
#print(mylist)

#【4】
#追加元素,通过.append在尾部插入元素 .extend可以实现追加多个元素
#mylist.append("d")
#print(mylist)
#mylist.extend([1,2,3])
#print(mylist)
"""
#【5】 指定下标
# 删除元素 del列表[下标]或者.pop(下标)
del mylist [1]
print(mylist)
mylist = ["a","b","c"]
mylist.pop(2)
print(mylist)

# 【6】 指定元素
# remove删除某元素第一次出现的时候
mylist = ["a","b","a","c"]
mylist.remove("a")
print(mylist)

# 【7】
# clear清空列表
mylist.clear()
print(mylist)

# 【8】
# count同级某列表的元素数量
mylist = ["a","b","a","c"]
count = mylist.count("a")
print(count)

# 【9】
# len数出列表的元素总数
len = len(mylist)
print(len)
"""

#将容器依次取出元素进行的操作叫遍历
my_list = ["a","b","c"]
index = 0
while index < len(my_list):
    element = my_list[index]
    print(f"列表的元素:{element}")
    index += 1

o_list = ["x","e","a"]
for element1 in o_list:
    print(f"列表的元素有：{element1}")