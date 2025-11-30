#输入数字找偶数
num = int(input("请输入数字"))
a = 0
for x in range(1,num+1):
    if x%2 == 0: #取余
        a += 1
print(f"1到{num}范围内，有{a}个偶数")