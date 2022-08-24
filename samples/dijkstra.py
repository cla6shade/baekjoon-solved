import heapq
start = 3 #시작 번호
graph = [] #그래프
INF = int(1e9)
distance = [INF] * 3


def dijkstra(start):
    q =[]
    heapq.heappush(q, (start,0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(i[0], cost)


print(distance)