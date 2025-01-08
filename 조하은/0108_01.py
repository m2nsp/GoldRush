# 2305 햄버거 분배

def solution(N, K, arr):
    answer = 0
    for i in range(N):
        if arr[i] == 'P':
            # 앞뒤로 K만큼 떨어진 거리에서 먹을 수 있는 햄버거가 있는지 탐색
            for j in range(i-K, i+K+1):
                if j < 0 or j >= N:
                    continue
                if arr[j] == 'H':
                    arr[j] = 0 # 햄버거를 먹으면 0으로 바꿈
                    answer += 1
                    break
    return answer

N, K = map(int, input().split())
arr = list(input())

print(solution(N, K, arr))
