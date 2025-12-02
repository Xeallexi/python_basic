import math

def forward_kinematics(joints: list) -> tuple:
    """
    正运动学：输入6个关节角（度），返回末端TCP位姿(x, y, z, roll, pitch, yaw)
    简化版：用假公式，但逻辑完全正确，可直接替换真实DH参数
    """
    # 假设一个6轴机械臂，L1~L6为连杆长度（随便设的）
    L1, L2, L3 = 100, 400, 350
    a1, a2, a3, a4, a5, a6 = [math.radians(j) for j in joints]  # 转弧度
    
    x = L2 * math.cos(a1) * math.cos(a2) + L3 * math.cos(a1) * math.cos(a2 + a3)
    y = L2 * math.sin(a1) * math.cos(a2) + L3 * math.sin(a1) * math.cos(a2 + a3)
    z = L1 + L2 * math.sin(a2) + L3 * math.sin(a2 + a3)
    
    # 姿态简化（真实项目再补）
    roll, pitch, yaw = 0, a2 + a3, a1
    
    return (x, y, z, math.degrees(roll), math.degrees(pitch), math.degrees(yaw))

def inverse_kinematics(x: float, y: float, z: float) -> list:
    """
    逆运动学：输入目标点(x,y,z)，返回一组可达的关节角（度）
    简化版：返回一个假解，但格式完全正确
    """
    # 真实逆解超复杂，这里返回一个“看起来合理”的假解
    import random
    fake_joints = [random.randint(-90, 90) for _ in range(6)]
    print("警告：当前为简化逆解，实际项目需使用专业算法")
    return fake_joints

def generate_trajectory(start: tuple, end: tuple, steps: int = 10) -> list:
    """
    直线轨迹插值：从起点到终点，生成 steps 个中间点
    """
    x1, y1, z1 = start
    x2, y2, z2 = end
    
    trajectory = []
    for i in range(steps + 1):
        ratio = i / steps
        x = x1 + (x2 - x1) * ratio
        y = y1 + (y2 - y1) * ratio
        z = z1 + (z2 - z1) * ratio
        trajectory.append((round(x, 2), round(y, 2), round(z, 2)))
    
    return trajectory

def print_pose(pose: tuple):
    """美观打印位姿"""
    x, y, z, roll, pitch, yaw = pose
    print(f"\n=== 末端位姿 ===")
    print(f"位置：X={x:8.2f}  Y={y:8.2f}  Z={z:8.2f} mm")
    print(f"姿态：R={roll:8.2f}  P={pitch:8.2f}  Y={yaw:8.2f} °")

def main():
    print("=== 欢迎使用机械臂运动计算器 v1.0 ===")

    while True:
        print("\n" + "="*50)
        print("1. 正运动学    2. 逆运动学")
        print("3. 轨迹规划    4. 退出")
        choice = input("请选择功能（1-4）：")
        
        if choice == "1":
            joints = input("请输入6个关节角（用空格分开，如 0 30 45 0 90 0）：")
            joints = [float(x) for x in joints.split()]
            if len(joints) != 6:
                print("错误：必须输入6个关节角！")
                continue
            pose = forward_kinematics(joints)
            print_pose(pose)
            
        elif choice == "2":
            coords = input("请输入目标点坐标 x y z（空格分开）：")
            x, y, z = map(float, coords.split())
            joints = inverse_kinematics(x, y, z)
            print(f"逆解关节角：{joints}")
            
        elif choice == "3":
            print("请输入起点坐标 x y z：")
            start = tuple(map(float, input().split()))
            print("请输入终点坐标 x y z：")
            end = tuple(map(float, input().split()))
            steps = int(input("插值点数（默认10）：") or "10")
            traj = generate_trajectory(start, end, steps)
            print(f"\n生成 {len(traj)} 个轨迹点：")
            for i, point in enumerate(traj):
                print(f"  {i+1:2d}: {point}")
                
        elif choice == "4":
            print("机械臂已下班！明天继续卷！")
            break
        else:
            print("输入错误！请选1-4！")

# 启动程序
if __name__ == "__main__":
    main()
