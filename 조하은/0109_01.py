def n_queens(n, row, board):
    # n개의 퀸을 모두 배치했다면 +1
    if row == n:
        return 1

    cnt = 0
    # row번째 행의 모든 열을 탐색
    for col in range(n):
        # row번째 행 col번째 열에 퀸을 배치할 수 있는지 체크
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(row - i):
                break
        else:
            # 가능하다면 퀸을 배치하고 재귀 호출
            board[row] = col
            cnt += n_queens(n, row + 1, board)

    return cnt

def solution(n):
    board = [0] * n
    return n_queens(n, 0, board)
