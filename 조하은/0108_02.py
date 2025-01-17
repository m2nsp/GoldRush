# 2306 가장 큰 정사각형 찾기

def solution(board):
    answer = 0
    for i in board:
        answer = max(i)

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]>0:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                answer = max(answer, board[i][j])
                    
    return answer**2
