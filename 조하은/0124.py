# 2103 프린터 큐

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    queue = deque()
    
    # 덱에 [우선순위, 프린터] 넣기
    for i in range(n):
        queue.append([temp[i], i])
    
    cnt = 0
    while True:
        # 우선순위가 더 높은게 있으면 제일 뒤로 보냄
        if queue[0][0]<max(queue)[0]:
            queue.append(queue.popleft())
        else:
            # 없으면 인쇄
            cnt += 1
            if queue.popleft()[1] == m:
                break
    print(cnt)
