from collections import deque

words = input()

words = words.split()

wordqueue = deque()

for word in words:
    wordqueue.appendleft(word)

print(wordqueue)

while wordqueue:
    answer = wordqueue.pop()
    if "o" in answer:
        print(answer)