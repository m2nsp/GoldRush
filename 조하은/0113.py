def solution(s):
    n = len(s)
    
    if n == 1:
        return 1
    
    answer = ""
    for i in range(1, n):
        temp = ""
        j = 0
        cnt = 1
        while True:
            if j+i > n:
                temp += s[j:]
                break
            if s[j:j+i] == s[j+i:j+i*2]:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt) + s[j:j+i]
                    cnt = 1
                else:
                    temp += s[j:j+i]
            j += i

        if len(answer)==0 or len(temp)<len(answer):
            answer = temp
            
    return len(answer)
