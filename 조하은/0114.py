# 2310 공유기 설치

def solution(N, C, X):
    X.sort()
    
    s = 1
    e = X[-1] - X[0]
    answer = 0
    
    while s <= e:
        mid = (s + e) // 2
        now = X[0]
        cnt = 1
        
        for i in range(1, N):
            if X[i] >= now + mid:
                cnt += 1
                now = X[i]
        
        if cnt >= C:
            s = mid + 1
            answer = mid
        else:
            e = mid -1

    return answer

N, C = map(int, input().split())
X = [0]*N

for i in range(N):
    X[i] = int(input())

print(solution(N, C, X))
