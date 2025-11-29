replies = {
    7 : "7有点幸运",
    13 :"13有点倒霉",
    99:"差点100"
}
print("欢迎")
name = input("你的名字是")
num = int(input("在1-100随机选一个数字"))
message = replies.get(num,f"{name},你输入的数字很特别")
print(message)
print(f"欢迎下次再来{name}")
