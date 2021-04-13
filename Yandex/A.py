import sys


J = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()

result = 0
j_set = set(J)

for c in S:
    if c in j_set:
        result += 1

print(result)
