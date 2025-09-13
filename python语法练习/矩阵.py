def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def main():
    # 输入矩阵A的行数和列数
    A1, B1 = map(int, input("请输入矩阵A的行数和列数（用空格分隔）：").split())

    # 输入矩阵B的行数和列数
    A2, B2 = map(int, input("请输入矩阵B的行数和列数（用空格分隔）：").split())

    # 检查矩阵是否可以相乘
    if B1 != A2:
        print("错误：矩阵的列数必须等于另一个矩阵的行数")
        return

    # 创建矩阵A
    A = []
    print("请输入矩阵A的元素（每行元素用空格分隔）：")
    for _ in range(A1):
        row = list(map(int, input().split()))
        A.append(row)

    # 创建矩阵B
    B = []
    print("请输入矩阵B的元素（每行元素用空格分隔）：")
    for _ in range(A2):
        row = list(map(int, input().split()))
        B.append(row)

    # 计算矩阵乘法
    result = matrix_multiply(A, B)

    # 打印结果矩阵
    print("矩阵乘法的结果为：")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()