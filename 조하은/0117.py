# 2206 3*n 타일링

def solution(n):
    DP = [0]*(n//2+1)
    DP[0] = 1
    DP[1] = 3
    for i in range(2, n//2+1):
        DP[i] = (DP[i-1]*4 - DP[i-2])%1000000007
        
    return DP[n//2]
