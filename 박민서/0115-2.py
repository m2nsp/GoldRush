# 24-2 상-1 평범한 배낭 (백준 12865)
N, k = map(int, input().split())

things = []  # 주어진 값 저장

for _ in range(N):
    w, v = map(int, input().split())  # w: 무게, v: 가치
    things.append((w, v))
    
# DP 배열 초기화
dp = [0] * (k + 1)

# DP 계산
for weight, value in things:
    for w in range(k, weight - 1, -1):  # 역순으로 순회
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[k])
