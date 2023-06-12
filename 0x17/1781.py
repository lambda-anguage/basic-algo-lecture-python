import sys
from heapq import heappush, heappop, heappushpop
input = sys.stdin.readline

def solve():
    n = int(input())
    pq = []
    solved = []
    for _ in range(n):
        x, y = map(int, input().split())
        heappush(pq, (x, -y))
    for i in range(1, n + 1):
        if pq:
            heappush(solved, -heappop(pq)[1])
            while pq and pq[0][0] == i:
                _, y = heappop(pq)
                heappushpop(solved, -y)
        else:
            break
    print(sum(solved))


if __name__ == "__main__":
    solve()
