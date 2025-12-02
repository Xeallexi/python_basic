money = 50000000  
name = input("请输入姓名：") 
def remain():
    """查询余额功能"""
    print(f"\n{'='*10}查询余额{'='*10}")
    print(f"{name}你好，你的余额剩余：{money} 元")
def deposit():
    """存款功能"""
    print(f"\n{'='*10}存款{'='*10}")
    plus = int(input("请输入你要存的金额数量："))
    global money
    money += plus  # 余额 += 存款金额
    print(f"{name}，你好，你存款 {plus} 元成功！")
    print(f"当前余额剩余：{money} 元")
def withdrawal():
    """取款功能"""
    print(f"\n{'='*10}取款{'='*10}")
    minus = int(input("请输入你要取的金额数量："))
    global money
    if minus <= 0:
        print("错误：取款金额不能为负数！")
        return
    if minus > money:
        print("错误：余额不足，无法取款！")
        return
    money -= minus  
    print(f"{name}，你好，你取款 {minus} 元成功！")
    print(f"当前余额剩余：{money} 元")

def main():
    while True:  
        print(f"\n{'='*10}主菜单{'='*10}")
        print(f"{name}，你好，欢迎来到ATM，请选择操作：")
        print("1. 查询余额")
        print("2. 存款")
        print("3. 取款")
        print("4. 退出")
        option = int(input("请输入你的选择（1-4）："))
        if option == 1:
            remain()
        elif option == 2:
            deposit()
        elif option == 3:
            withdrawal()
        elif option == 4:
            print(f"\n{name}，感谢使用ATM，再见！")
            break
        else:
            print("输入错误！请选择1-4之间的数字！")
main()