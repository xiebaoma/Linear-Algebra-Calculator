import linear_system_solver

def main():
    while True:
        print("\n请选择操作：")
        print("1. 求解线性方程组")
        print("exit. 退出程序")

        user_choice = input("请输入选项：")

        if user_choice == '1':
            linear_system_solver.solve()
        elif user_choice.lower() == 'exit':
            print("程序退出")
            break
        else:
            print("无效选项，请重新输入")

if __name__ == "__main__":
    main()