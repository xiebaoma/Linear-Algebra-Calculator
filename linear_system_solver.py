import numpy as np

def gauss_elimination(matrix):
    # 检查输入矩阵的格式是否正确
    if not all(len(row) == len(matrix) + 1 for row in matrix):
        return "Input matrix format is incorrect. Please check the matrix."

    matrix = np.array(matrix, dtype=float)
    n = len(matrix)

    # 高斯消元法
    for i in range(n):
        # 找到当前列最大的元素，进行行交换
        max_row = np.argmax(abs(matrix[i:n, i])) + i
        matrix[[i, max_row]] = matrix[[max_row, i]]

        if matrix[i, i] == 0:
            # 如果矩阵的主对角元素为零，检查常数项
            if matrix[i, -1] == 0:
                return "The system of equations has infinitely many solutions"
            else:
                return "The system of equations has no solution"

        # 消去下三角元素
        for j in range(i + 1, n):
            factor = matrix[j, i] / matrix[i, i]
            matrix[j, i:] -= factor * matrix[i, i:]

    # 回代求解
    solution = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if matrix[i, i] == 0:
            # 如果有自由变量存在，说明无穷多解
            return "The system of equations has infinitely many solutions"
        solution[i] = (matrix[i, -1] - np.dot(matrix[i, i + 1:n], solution[i + 1:n])) / matrix[i, i]
    
    return solution

def solve():
    while True:
        # 输入增广矩阵
        user_input = input("请输入增广矩阵 (或输入 'exit' 退出)：")

        if user_input.lower() == 'exit':
            print("程序退出")
            break

        try:
            matrix = eval(user_input)
        except Exception as e:
            print(f"输入格式错误: {e}")
            continue

        if isinstance(matrix, list) and all(isinstance(row, list) for row in matrix):
            result = gauss_elimination(matrix)
            if isinstance(result, str):
                print(result)
            else:
                print("方程组的解为：", result)
        else:
            print("输入格式错误，请重新输入")
