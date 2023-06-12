import sys
from heapq import heappush, heappushpop

def solve():
    input = sys.stdin.readline
    n = int(input())
    pq = []

    for _ in range(n):
        for i in map(int, input().split()):
            if len(pq) < n:
                heappush(pq, i)
            else:
                heappushpop(pq, i)
    print(pq[0])
if __name__ == "__main__":
    solve()
