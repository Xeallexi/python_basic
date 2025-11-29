#布尔类型
"""
result = 10 > 5
print(result)
bool_1 = True

print(f"bool_1的内容是{bool_1},类型是{type(bool_1)}")
"""
#比较运算符 == != > < >= <=
"""
name1 = "aab"
name2 = "aaa"
print(f"name1 > name2的结果是{name1>name2}")
"""
#if语句

#age = int(input("输入你的年龄"))
#if age>=18:
 #print("你已成年")
#else:
 #print("你没成年")
"""
age = 2
print(f"今年我已经{age}")
if age>=18:
    print("已经成年了")
print("时间过得真快")
"""
#if 和 elif 同级 判断互斥且有顺序

#判断语句的嵌套
#通过空格缩进
"""
if int(input("你的身高是多少："))>120:
    print("身高超出限制，若vip等级达标可以免费")
    if int(input("你的vip等级："))>3:
        print("vip等级达标可以免费")
    else:
        print("抱歉，你要买票")
else: 
    print("欢迎免费游玩")
"""
age = int(input("输入年龄"))
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你符合年龄条件")
        if int(input("入职时间"))>2:
            print("可以")
        elif int(input("级别"))>3:
            print("可以")
        else:
            print("gun")
else:
    print("gun")