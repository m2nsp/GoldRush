# 23회 기출 3번
def solution(board, moves):
    arr = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            # 인형이 있으면 추가
            if board[i][move-1]!=0:
                if arr and arr[-1]==board[i][move-1]:
                    # 같은거면 제거
                    arr.pop()
                    answer += 2
                else:
                    # 다른거면 추가
                    arr.append(board[i][move-1])
                
                board[i][move-1] = 0
                break
            
    return answer
