# 24-1 중-2 문자열압축

def solution(s):
    # 데이터 초기화
    fixed_s = ""    # 수정된 문자열 저장하는 변수
    prev = ""       # 바로 전 잘라진 부분
    cut = ""        # 지금 잘라진 부분
    length = len(s) # 제일 처음 잘라진 단위
    cnt = 1         # 중복되는 단위 개수 저장
    answer = len(s)
    
    for step in range(1, ((len(s)//2)+1)):  # step: 자르는 기준 변수
        for j in range(0, len(s)+1, step):
            cut = s[j: j+step]
            if prev == cut:
                cnt += 1
                continue
            elif prev != cut and cnt >= 2:
                prev = str(cnt) + prev
            fixed_s += prev
            prev = cut
            cnt = 1
        fixed_s += prev
        answer = min(len(fixed_s), length)      #length 이전의 최소 단위개수
        length = answer
        fixed_s = ""
        prev=cut=""
    return answer
    
print(solution("a"))
