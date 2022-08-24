from collections import deque

n, k = list(map(int, input().split()))
dist = {}


def bfs():
    global n, k, visited
    sec = 0
    q = deque()
    q.append(n)
    dist[n] = 0

    while q:
        a = q.popleft()
        sec += 1
        nodes = [a - 1, a + 1, a * 2]
        for i in nodes:
            if i in dist or i > 100000 or i < 0:
                continue
            dist[i] = dist[a] + 1
            if i == k:
                return True
            q.append(i)
    return False


tf = bfs()
print(dist[k])
