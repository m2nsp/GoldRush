# 2207 외판원 순회2

import sys
input = sys.stdin.readline

def dfs(now, cnt, total_cost):
    global result
    
    # n개의 도시를 순회했고 현재 위치가 시작위치가 아니라면 최솟값 업데이트
    if cnt == n and W[now][0] > 0:
        result = min(result, total_cost + W[now][0])
        return
    
    # 현재 비용이 이미 현재 최솟값보다 큰 경우
    if total_cost >= result:
        return
    
    # 다른 도시 탐색
    for next in range(n):
        # 아직 방문하지 않았고, 가는 경로가 있다면 방문
        if not visited[next] and W[now][next] > 0:
            visited[next] = True
            dfs(next, cnt + 1, total_cost + W[now][next])
            visited[next] = False

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
result = sys.maxsize
visited = [False]*n

# 시작점 방문
visited[0] = True
dfs(0, 1, 0)

print(result)
