import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
pq = []
for _ in range(n):
    k = int(input())
    if k > 0:
        heappush(pq, k)
    else:
        print(heappop(pq) if pq else 0)
