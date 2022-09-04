from collections import deque

n, m, start = list(map(int, input().split()))
graph = {}
for _ in range(0, m):
    a, b = list(map(int, input().split()))
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

def bfs():
    q = deque()
    q.append(start)
    visited = []
    res = ""
    while q:
        a = q.popleft()
        visited.append(a)
        if res == "":
            res = str(a)
        else:
            res += " " + str(a)
        for b in graph[a]:
            if visited.count(b) == 0:
                q.append(b)
    return res


print(bfs())
