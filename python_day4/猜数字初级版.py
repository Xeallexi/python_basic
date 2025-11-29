print("欢迎来到猜数字，请你从1-10猜一个数字")
import random
num = random.randint(1,10)
guess = int(input("请输入："))
if guess != num:
    if guess < num:
        print("小了")
        guess_1 = int(input("请输入："))
        if guess_1 < num:
            print("小了")
            guess_2 = int(input("请输入："))
            if guess_2 != num:
                print(f"重来，正确答案是{num}")
            else:
                 print(f"恭喜你猜中了，数字就是{num}")
        elif guess_1 > num:
            print("大了")
            guess_2 = int(input("请输入："))
            if guess_2 != num:
                print(f"重来，正确答案是{num}")
            else:
                 print(f"恭喜你猜中了，数字就是{num}")
        else:
            print(f"恭喜你猜中了，数字就是{num}")
    elif guess > num:
        print("大了")
        guess_1 = int(input("请输入："))
        if guess_1 < num:
            print("小了")
            guess_2 = int(input("请输入："))
            if guess_2 != num:
                print(f"重来，正确答案是{num}")
            else:
                 print(f"恭喜你猜中了，数字就是{num}")
        elif guess_1 > num:
            print("大了")
            guess_2 = int(input("请输入："))
            if guess_2 != num:
                print(f"重来，正确答案是{num}")
            else:
                 print(f"恭喜你猜中了，数字就是{num}")
        else:
            print(f"恭喜你猜中了，数字就是{num}")
else:
    print(f"恭喜你猜中了，数字就是{num}")