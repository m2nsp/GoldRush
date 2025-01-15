# 24-1 하-1 행운의 바퀴
n, k = map(int, input().split())
wheel = ["?"] * n
start_idx = 0
answer = ""
used_chars = set()  # 사용된 문자를 저장할 집합

for i in range(k):
    change, result = input().split()
    new_idx = (start_idx - int(change)) % n
    if wheel[new_idx] != result and wheel[new_idx] != "?":
        answer = "!"
        break
    elif result != "?" and result in used_chars and wheel[new_idx] != result:  # 중복 문자 검사
        answer = "!"
        break
    else:
        wheel[new_idx] = result
        if result != "?":
            used_chars.add(result)  # 사용된 문자 추가
    start_idx = new_idx

if answer == "!":
    print(answer)
else:
    answer = wheel[start_idx:] + wheel[:start_idx]
    print("".join(answer))
