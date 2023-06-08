import sys
input = sys.stdin.readline
n = int(input())

def check(word):
    s = []
    for c in word:
        if len(s) > 0 and s[-1] == c:
            s.pop()
        else:
            s.append(c)
    return 1 if len(s) == 0 else 0

ret = 0
for _ in range(n):
    ret += check(input().rstrip())
print(ret)
