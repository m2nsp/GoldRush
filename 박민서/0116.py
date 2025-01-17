#백준 10799 - 24-1 하-3 쇠막대기

s = list(input())    #입력 값 받는 리스트
stack = []           # ( 개수 저장 리스트
answer = 0           # 정답 반환 변수

for i in range(len(s)):
    if s[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if s[i-1] == "(":            #레이저인 경우
            answer += len(stack)
        else:                        #쇠막대가 끝나는 경우
            answer += 1

print(answer)
