# 2303, 2002 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0      #터진 인형개수
    depth = len(board)  #인형 뽑기 기계 깊이
    pick = []       # 뽑힌 인형 리스트
    for move in moves:
        for j in range(depth):
            if board[j][move - 1] != 0:
                if pick and pick[-1] == board[j][move - 1]:
                    pick.pop()
                    answer += 2
                else:
                    pick.append(board[j][move - 1])
                board[j][move - 1] = 0  # 뽑은 인형 제거
                break
    return answer
