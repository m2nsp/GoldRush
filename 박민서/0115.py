#24-2 중-3 가장 큰 정사각형 찾기
def solution(board):
    board_length = len(board)
    row_length = len(board[0])
    dp = [[0 for _ in range(row_length+1)] for _ in range(board_length+1)]
    l = 0   # 가장 큰 정사각형의 한 변의 길이 나타내는 변수
    
    for i in range(1, board_length+1):
        for j in range(1, row_length+1):
            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
            #최댓값 구하기
            l = max(l, dp[i][j])
    answer = l*l
    return answer
