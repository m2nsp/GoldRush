# 2201 행운의 바퀴

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

wheel = ["?"]*N # 바퀴
idx = 0 # 화살표 위치
isLuckyWheel = True # 행운의 바퀴가 맞는지 여부

for _ in range(K):
    S, letter = input().split()
    
    # 행운의 바퀴가 이미 아닌 경우 입력만 받고 continue
    if not isLuckyWheel:
        continue
    
    idx = (idx - int(S))%N # 화살표 위치 계산
    
    if wheel[idx] == "?":
        # 중복 글자 체크
        if letter in wheel:
            isLuckyWheel = False
        else:
            wheel[idx] = letter
    elif wheel[idx] == letter:
        continue
    else:
        isLuckyWheel = False
    
if not isLuckyWheel:
    print("!")
else:
    for i in range(N):
        print(wheel[(idx+i)%N], end="")
    
