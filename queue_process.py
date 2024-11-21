from collections import deque

words = input()

words = words.split()

wordqueue = deque(words)

print(wordqueue)

while wordqueue:
    answer = wordqueue.pop()
    if "o" in answer:
        print(answer)