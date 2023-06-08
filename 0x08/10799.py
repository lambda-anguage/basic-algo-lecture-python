import sys
input = sys.stdin.readline

x = input().rstrip()
s = []
prev = ""
ret = 0

for c in x:
    if c == ")":
        if prev == "(":
            s.pop()
            ret += len(s)
        else:
            s.pop()
            ret += 1
    else:
        s.append(c)
    prev = c

print(ret)

