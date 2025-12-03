import json
import os

FILE = "bank.data.json"

# 初始化用户数据（从文件读取或创建空字典）
if os.path.exists(FILE):
    with open(FILE, "r", encoding="UTF-8") as f:
        users = json.load(f)
else:
    users = {}

def save_data():
    """保存用户数据到文件"""
    with open(FILE, "w", encoding="UTF-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def remain(name):
    """查询余额功能（接收当前用户名作为参数）"""
    print(f"\n{'='*10}查询余额{'='*10}")
    # 直接从users字典获取当前用户余额（无需global money）
    money = users[name]
    print(f"{name}你好，你的余额剩余：{money} 元")

def deposit(name):
    """存款功能（接收当前用户名作为参数）"""
    print(f"\n{'='*10}存款{'='*10}")
    # 校验输入是否为正整数
    while True:
        plus_input = input("请输入你要存的金额数量（正整数）：")
        if plus_input.isdigit():
            plus = int(plus_input)
            break
        print("输入错误！请输入正整数金额！")
    
    # 直接修改users字典中当前用户的余额
    users[name] += plus
    # 存款后保存数据到文件
    save_data()
    print(f"{name}，你好，你存款 {plus} 元成功！")
    print(f"当前余额剩余：{users[name]} 元")

def withdrawal(name):
    """取款功能（接收当前用户名作为参数）"""
    print(f"\n{'='*10}取款{'='*10}")
    # 校验输入是否为正整数
    while True:
        minus_input = input("请输入你要取的金额数量（正整数）：")
        if minus_input.isdigit():
            minus = int(minus_input)
            break
        print("输入错误！请输入正整数金额！")
    
    # 校验余额是否充足
    if minus > users[name]:
        print("错误：余额不足，无法取款！")
        return
    
    # 直接修改users字典中当前用户的余额
    users[name] -= minus
    # 取款后保存数据到文件
    save_data()
    print(f"{name}，你好，你取款 {minus} 元成功！")
    print(f"当前余额剩余：{users[name]} 元")

def main():
    print("===欢迎使用ATM===")
    while True:
        # name是main函数的局部变量，无需global
        name = input("请输入你的姓名(输入exit退出）：")
        if name == "exit":
            print("感谢你的使用，再见")
            break
        # 新用户创建（初始余额500000元）
        if name not in users:
            print(f"欢迎新用户{name}，为你创建账户，初始余额500000元！")
            users[name] = 500000
            save_data()  # 新用户创建后保存
        
        # 子循环：登录后的操作菜单
        while True:
            print(f"\n{'='*10}主菜单{'='*10}")
            print(f"{name}，你好，欢迎来到ATM，请选择操作：")
            print("1. 查询余额")
            print("2. 存款")
            print("3. 取款")
            print("4. 退出当前账户")
            
            # 校验菜单输入是否为1-4的整数
            while True:
                option_input = input("请输入你的选择（1-4）：")
                if option_input.isdigit():
                    option = int(option_input)
                    if 1 <= option <= 4:
                        break
                print("输入错误！请选择1-4之间的数字！")
            
            # 根据选择调用对应功能（传入当前用户名name）
            if option == 1:
                remain(name)
            elif option == 2:
                deposit(name)
            elif option == 3:
                withdrawal(name)
            elif option == 4:
                print(f"\n{name}，感谢使用ATM，再见！")
                break  # 退出当前账户，返回姓名输入界面

# 关键：在main函数定义外部调用（避免递归死循环）
if __name__ == "__main__":
    main()