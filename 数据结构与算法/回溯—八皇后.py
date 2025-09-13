import matplotlib.pyplot as plt
import numpy as np


# 画出一个棋盘并放置皇后
def visualize_solution(board):
    n = len(board)
    chessboard = np.zeros((n, n))

    # 在棋盘上标记皇后位置
    for i in range(n):
        chessboard[i][board[i]] = 1

    # 可视化棋盘
    plt.figure(figsize=(6, 6))
    plt.imshow(chessboard, cmap='binary', extent=[0, n, 0, n])

    # 设置标题
    plt.title('Solution to the 8-Queens Problem')

    # 显示棋盘格子
    for i in range(n):
        for j in range(n):
            plt.text(j, i, 'Q' if chessboard[i][j] == 1 else '', ha='center', va='center', fontsize=12, color='red')

    plt.xticks(range(n))
    plt.yticks(range(n))
    plt.grid(True)
    plt.show()


# 判断当前位置是否安全
def is_safe(board, row, col):
    for i in range(row):
        # 检查列是否已经有皇后
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


# 回溯算法求解所有可能的解
def solve_queens(board, row, solutions):
    n = len(board)

    if row == n:  # 所有皇后都放置完成
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1, solutions)
            # 回溯，撤销当前放置
            board[row] = -1


# 主函数
def solve_and_visualize_queens(n=8):
    board = [-1] * n  # 创建棋盘，-1表示没有皇后
    solutions = []  # 存储所有解
    solve_queens(board, 0, solutions)

    # 可视化所有解
    for solution in solutions:
        visualize_solution(solution)


# 执行
solve_and_visualize_queens(8)
