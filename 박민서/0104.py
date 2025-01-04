# 2302, 2001 ATM

def solution(n, p):
    p.sort()
    sum = [0]*n                # 합배열 생성
    sum[0] = p[0]
    for i in range(1, n):
        sum[i] = sum[i-1]+p[i]
    ans = 0
    for i in range(n):         # 최소 합 구하기
        ans += sum[i]      
    return ans
