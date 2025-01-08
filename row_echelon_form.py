from fractions import Fraction

def row_echelon_form(matrix):
    rows, cols = len(matrix), len(matrix[0])
    matrix = [[Fraction(x) for x in row] for row in matrix]

    lead = 0  # 主元所在的列
    for r in range(rows):
        if lead >= cols:
            break
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if lead == cols:
                    return matrix
                continue
        matrix[r], matrix[i] = matrix[i], matrix[r]

        lv = matrix[r][lead]
        matrix[r] = [mrx / lv for mrx in matrix[r]] # 将主元化为1

        for i in range(rows):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for iv, rv in zip(matrix[i], matrix[r])]
        lead += 1
    return matrix

def is_valid_matrix(input_str):
    """检查输入的矩阵格式是否正确"""
    try:
        # 尝试将字符串转换为列表的列表形式
        matrix = eval(input_str)
        # 检查矩阵是否为二维列表
        if isinstance(matrix, list) and all(isinstance(row, list) for row in matrix):
            # 检查所有行的长度是否一致
            row_length = len(matrix[0])
            if all(len(row) == row_length for row in matrix):
                return True, matrix
            else:
                return False, "矩阵的每一行长度必须相同"
        else:
            return False, "输入格式错误，请输入一个二维列表"
    except Exception as e:
        return False, f"输入解析错误: {e}"

def solve():
    while True:
        print("\n请输入一个增广矩阵进行简化阶梯形矩阵（输入exit退出）：")

        user_input = input("请输入矩阵：")

        if user_input.lower() == 'exit':
            print("程序退出")
            break

        valid, result = is_valid_matrix(user_input)

        if not valid:
            print(result)
            continue

        matrix = result

        # 处理并简化阶梯形矩阵
        simplified_matrix = row_echelon_form(matrix)

        # 输出简化后的阶梯形矩阵
        print("简化后的阶梯形矩阵：")
        for row in simplified_matrix:
            output_row = []
            for x in row:
                if x.denominator == 1:  # 如果分母是1，则为整数
                    output_row.append(int(x)) # 输出整数部分
                else:
                    output_row.append(str(x)) # 否则输出分数形式
            print(output_row) # 直接打印列表，元素会自动以空格分隔
