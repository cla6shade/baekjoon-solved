import heapq
import sys
input = sys.stdin.readline

v, e = list(map(int, input().split()))
start = int(input())
graph = [[] for _ in range(v+1)]

INF = int(1e9)
dp = [INF] * (v+1)

for i in range(e):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))

def dijkstra():
    global graph, start, dp
    q = []
    dp[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dp[now] < dist:
            continue
        for i in graph[now]:
            # i => next, dist
            cost = dist + i[1]
            if cost < dp[i[0]]:
                dp[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()

for j in range(v+1):
    if j==0:
        continue
    if dp[j] == INF:
        print("INF")
    else:
        print(dp[j])
