import sys
input = sys.stdin.readline

def solve():
    x = input().rstrip()
    s = [["", 0]]
    for c in x:
        if c == ")":
            if s[-1][0] != "(":
                return 0
            tmp = s.pop()[1]
            s[-1][1] += tmp * 2 if tmp > 0 else 2
        elif c == "]":
            if s[-1][0] != "[":
                return 0
            tmp = s.pop()[1]
            s[-1][1] += tmp * 3 if tmp > 0 else 3
        else:
            s.append([c, 0])
    return s[0][1] if len(s) == 1 else 0

print(solve())
