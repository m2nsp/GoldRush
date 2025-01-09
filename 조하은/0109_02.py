# 2308 평범한 배낭

def solution(n, k, W, V):
    D = [[0]*(k+1) for _ in range(n+1)]
    
    # DP 테이블 채우기
    for i in range(1, n+1):
        for j in range(1, k+1):
            # 현재 물건을 배낭에 넣을 수 있는지 확인
            if W[i-1]<=j:
                # 넣을 수 있다면 넣지 않은 경우와 넣은 경우 중 가치가 더 큰 값을 저장
                D[i][j] = max(D[i-1][j], D[i-1][j-W[i-1]]+V[i-1])
            else:
                # 넣지 못하면 그대로
                D[i][j] = D[i-1][j]
    
    return D[n][k]

n, k = map(int, input().split())
W = [0]*n
V = [0]*n

for i in range(n):
    W[i], V[i] = map(int, input().split())

print(solution(n, k, W, V))
