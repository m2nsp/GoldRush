# 2302, 2202 팰린드롬 만들기 

def solution(name):
    counts = {}
        
    # 딕셔너리에 알파벳과 개수 저장
    for i in range(len(name)):
        if name[i] in counts:
            counts[name[i]] += 1
        else:
            counts[name[i]] = 1
    
    middle = -1
    temp = ""
    letters = sorted(counts.keys())
    
    # 글자의 길이가 홀수라면 홀수개인 문자는 하나, 짝수라면 없어야함
    for i in range(len(letters)):
        if counts[letters[i]]%2==1:
            if middle != -1:
                # 홀수개인 문자가 하나 이상이면 팰린드롬 만들 수 없음
                return "I'm Sorry Hansoo"
            middle = i
        for j in range(counts[letters[i]]//2):
            temp += letters[i]
    
    # 팰린린드롬 만들기
    answer = ""

    # 길이가 홀수면 중간 문자 추가
    if middle!=-1:
        answer = temp + letters[middle]
    answer += temp[::-1]
    
    return answer
    
if __name__ == "__main__":
    name = input()
    print(solution(name))
