from collections import deque

numbers = list(map(int, input().split()))

numberstack = deque()

for n in numbers:
    numberstack.append(n)

print(numberstack)

while numberstack:
    exp = numberstack.pop()
    answer = exp * exp 
    print(answer)