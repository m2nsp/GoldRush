# 중-1. 가장많이받은선물
def solution(friends, gifts):
    n = len(friends)   # 친구 수
    gift_matrix = [[0]*n for _ in range(n)]  # 선물 주고받은 현황 저장하는 2차원 배열
    gift_score = [0]*n    # 선물 지수
    next_month = [0]*n   # 다음달에 받는 선물 수 저장하는 리스트
    
    friend_to_index = {}
    for i, friend in enumerate(friends):
        friend_to_index[friend] = i
    
    for gift in gifts:
        # 준 선물, 받은 선물 내역 저장
        giver, receiver = gift.split() 
	      giver_idx = friend_to_index[giver]
        receiver_idx = friend_to_index[receiver]
        gift_matrix[giver_idx][receiver_idx] += 1
        # 선물 지수 업데이트
        gift_score[giver_idx] += 1
        gift_score[receiver_idx] -= 1
    
    for i in range(n):
        for j in range(i+1, n):
            # i가 j에게 준 선물이 더 많을 때
            if gift_matrix[i][j] > gift_matrix[j][i]:
                next_month[i] += 1
            # j가 i에게 준 선물이 더 많을 때
            elif gift_matrix[i][j] < gift_matrix[j][i]:
                next_month[j] += 1
            # 같거나 0일 경우
            else:
            # 선물 지수가 높은 사람이 받음
                if gift_score[i] > gift_score[j]:
                    next_month[i] += 1
                elif gift_score[i] < gift_score[j]:
                    next_month[j] += 1
                    
    return max(next_month)
