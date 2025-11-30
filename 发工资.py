sum = 10000
a = 0
for i in range(1,21):
    import random
    num = random.randint(1,10)
    if num<5:
        print(f"员工{i},绩效分{num}，低于5，不发工资下一位")
        continue
    else:
        a += 1
        print(f"向员工{i}，账户余额剩余{sum-a*1000}")
        if sum-a*1000== 0:
            print("工资发完了")
            break