# 2205 강의실 배정

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

classes.sort() # 시작 시간이 빠른 순으로 정렬

queue = []
heappush(queue, classes[0][1])

for i in range(1, n):
    if classes[i][0] >= queue[0]:
        heappop(queue) # 강의 시간이 겹치지 않으면 pop
    heappush(queue, classes[i][1]) #새로운 강의실 추가

print(len(queue))
