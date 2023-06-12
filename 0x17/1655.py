import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
min_heap, max_heap = [], []

for _ in range(n):
    k = int(input())
    if len(min_heap) < len(max_heap):
        heappush(min_heap, k)
    else:
        heappush(max_heap, -k)
    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        x, y = -heappop(max_heap), heappop(min_heap)
        heappush(min_heap, x)
        heappush(max_heap, -y)
    print(-max_heap[0])
