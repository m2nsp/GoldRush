# 2208 뱀

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]

# 보드에 사과 위치 저장 (-1은 사과를 뜻함)
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = -1

l = int(input())
directions = deque()
for i in range(l):
    x, c = input().split()
    directions.append([int(x), c])

snake = deque([(0, 0)])
board[0][0] = 1 # 1이면 뱀을 뜻함

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

idx = 0
cnt = 0
while True:        
    cnt += 1
    head = snake[0] # 뱀의 머리 위치

    # 뱀이 이동할 인덱스 계산
    x = head[1]+dx[idx]
    y = head[0]+dy[idx]

    # 보드를 벗어나거나 몸통에 부딪히면 게임 종료
    if not (0<=x<n and 0<=y<n) or board[y][x]==1:
        break

    snake.appendleft((y, x)) # 한 칸 이동하기

    # 이동한 칸에 사과가 없으면 꼬리 이동
    if board[y][x]==0:
        tail = snake.pop()
        board[tail[0]][tail[1]] = 0
    
    board[y][x] = 1 # 보드에 이동한거 표시

    # 다음 방향 계산
    if directions and cnt == directions[0][0]:
        if directions[0][1]=='D':
            idx = (idx+1)%4
        elif directions[0][1]=='L':
            idx = (idx-1)%4
        directions.popleft()

print(cnt)
