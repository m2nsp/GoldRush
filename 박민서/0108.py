# 하-2 : 펠린드롬
def make_palindrome(s):
    # 문자열을 정렬
    sorted_s = sorted(s)
    
    # 팰린드롬의 앞부분과 중앙 문자를 저장할 변수
    palindrome_half = []
    center = ''
    
    # 정렬된 문자열을 순회하며 팰린드롬 구성
    i = 0
    while i < len(sorted_s):
        # 현재 문자의 개수를 세기
        count = 1
        while i + 1 < len(sorted_s) and sorted_s[i] == sorted_s[i + 1]:
            count += 1
            i += 1
        
        # 짝수 개수만큼 팰린드롬 앞부분에 추가
        palindrome_half.extend([sorted_s[i]] * (count // 2))
        
        # 홀수 개수인 경우 중앙 문자로 저장
        if count % 2 == 1:
            if center:               # 이미 center 값이 존재 (= 홀수 개수 2개 이상)
                return "I'm Sorry Hansoo"
            center = sorted_s[i]     # center 존재하지 않을 경우, 중앙문자로 저장
        
        i += 1
    
    # 최종 팰린드롬 구성
    return ''.join(palindrome_half + [center] + palindrome_half[::-1])

# 사용 예
input_string = input()
print(make_palindrome(input_string))
