# 2301, 2001 ATM

import sys
input = sys.stdin.readline

def solution(P):
    P.sort()
    sum = 0
    temp = 0
    
    for i in range(N):
        temp += P[i]
        sum += temp
    
    return sum

N = int(input())
P = list(map(int, input().split()))
print(solution(P))
