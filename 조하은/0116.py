# 2203 쇠막대기

arr = input()
stack = []
result = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if arr[i-1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)
