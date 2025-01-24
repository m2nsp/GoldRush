#23-2 하-2 문자열 압축

def solution(s):
    n = len(s)        # 주어진 문자열 길이
    prev = s[0]       # 이전 문자 저장하는 변수
    result = ""       # 결과값 저장하는 변수
    cnt = 0           # 같은 문자 개수 저장하는 변수
    
    if prev == "1":   # 맨 앞 문자가 1인 경우
        result += '1'
    
    for i in range(1, n):   
        if prev == s[i]:    # 앞의 문자와 같은 경우
            cnt += 1
        else:
            k = chr(ord('A')+cnt)
            prev = s[i]
            cnt =  0    # cnt 초기화
            result += k
    result += chr(ord('A')+cnt)   # 마지막 값 저장
    return result
    
if __name__ == '__main__':
    s = input()
    answer = solution(s)
    print(answer)
