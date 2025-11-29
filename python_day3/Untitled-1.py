# 2025.11.28

#拼接字符串 用加号
#字面量之间的拼接
"""
print("xea" + "llex")
#字面量与字符串的拼接
name = "xea"
print("I am "+name)
tel = 222
#print(tel + "2222") 字符串不能与非字符串拼接
"""
"""
#字符串格式化 通过占位完成拼接
class_num = 22
message = "班级数是%s" %(class_num)
print(message)

num = 2023104080037
name = "zmx"
message = "我的姓名是%s,学号是%s" %(name,num)
print(message)
# %s将内容转换为字符串 %d转换成整数 %f浮点

name = "bitcoin"
price = 92000.88
message = "%s的现价是:%f" %(name,price)
print(message)
"""

"""
#字符串的精度控制
#m.n m控制宽度 n控制小数点精度
name = "bitcoin"
price = 92000.88
message = f"{name}的现价是:{price}"
print(message)
#f可以快速格式化 进行占位 不理会类型 不会精度计算
name = "bitcoin"
price = 92000.88
print(f"{name}的现价是{price}")
"""

#表达式格式化
#print("5**100的结果是%d"%(5**100))
"""
name = "zmx"
stock_price = 20
stock_code = 88888
stock_price_daily_growth_factor = 1.2
growth_days = 29
final = stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司：{name}，股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是%.1f。经过%d天的增长后。现价%.2f" %(stock_price_daily_growth_factor,growth_days,final))
"""
"""
#input
print("whats your name")
name = input()
print(f"ok{name}")
"""