# 중-2 햄버거분배

n, k = map(int, input().split())
s = input()

A = list(s)  # 문자열을 리스트로 변환
cnt = 0

for i in range(n):
    if A[i] != "P":
        continue  # 사람이 아니면 넘어감
    # k 거리 내의 햄버거를 찾음
    for d in range(max(0, i-k), min(n, i+k+1)):  # 범위를 제한하여 검사
        if d != i and A[d] == "H":
            cnt += 1
            A[d] = 0  # 햄버거를 소진 처리
            break

print(cnt)
