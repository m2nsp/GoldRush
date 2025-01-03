#2301 나누고 나누기

def solution(a, b, c, d):
    count = 0               # 찾는 수의 개수
    for i in range(a, b+1):
        if i%c==0 and i%d!=0:   # 조건만족 시
            count += 1          # 개수 증가
    return count

print(solution(12, 18, 3, 5))
print(solution(1, 10, 2, 1))
