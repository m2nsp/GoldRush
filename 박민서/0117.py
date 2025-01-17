# 24-2 중-2 강의실 배정 (백준 11000번)

import heapq
classTime = []
N = int(input())
ans = []

for i in range(N):                        # 주어진 Si, Ti 저장
    a, b = map(int, input().split())
    classTime.append([a, b])

classTime.sort()        

heapq.heappush(ans, classTime[0][1])    # 처음 값 초기화

for i in range(1, N):
    if classTime[i][0] < ans[0]:
        heapq.heappush(ans, classTime[i][1])
    else:
        heapq.heappop(ans)
        heapq.heappush(ans, classTime[i][1])
        
print(len(ans))    
