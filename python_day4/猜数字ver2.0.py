import random
total_games = 0
total_guesses = 0
while True:
    num = random.randint(1,100)
    chance = 6
    time = 0
    total_games += 1
    total_guesses = 0
    print(f"第{total_games}局开始")
    while chance>0:
         guess = int(input("请输入猜的数字："))
         chance -= 1
         time += 1
         total_guesses += 1
         if guess < num:
              print("小了")
              print(f"还剩{chance}次机会") 
         elif guess > num:
              print("大了")
              print(f"还剩{chance}次机会") 
         elif guess == num:
              print(f"猜对了，答案就是{num}")
    else:
        print(f"机会用完，正确答案是{num}") 
    avg = total_guesses/total_games
    print(f"已经玩了{total_games}局了,平均{avg:.1f}次找到")
    flag = input("还要继续游玩吗(y/n):")
    if flag != "y":
         print("下次见")
         break

