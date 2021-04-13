import sys


n = int(sys.stdin.readline())
answer = 0
current_ones_len = 0

for i in range(n):
    number = int(sys.stdin.readline())
    if number == 1:
        current_ones_len += 1
    else:
        answer = max(current_ones_len, answer)
        current_ones_len = 0

    answer = max(current_ones_len, answer)

print(answer)
