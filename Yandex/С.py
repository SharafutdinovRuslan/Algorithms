import sys


n = int(sys.stdin.readline())
if n > 0:
    prev_number = int(sys.stdin.readline())
    print(prev_number)

for i in range(1, n):
    number = int(sys.stdin.readline())
    if number != prev_number:
        print(number)
        prev_number = number



