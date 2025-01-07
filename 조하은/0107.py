# 2304 가장 많이 받은 선물

def solution(friends, gifts):
    n = len(friends)
    friend_gift = [[0]*n for _ in range(n)] # 선물 주고 받은 내역
    gift_level = [0]*n # 선물 지수
    next_month = [0]*n # 다음 달에 받을 선물
    
    for gift in gifts:
        A, B = gift.split()
        idxA = friends.index(A)
        idxB = friends.index(B)
        friend_gift[idxA][idxB] += 1
        gift_level[idxA] += 1
        gift_level[idxB] -= 1
    
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if friend_gift[i][j] > friend_gift[j][i]:
                next_month[i] += 1
            elif friend_gift[i][j] == friend_gift[j][i]:
                if gift_level[i] > gift_level[j]:
                    next_month[i] += 1
    
    return max(next_month)
