from collections import deque

n = int(input())

graph = []

minh = 101
maxh = -1

for i in range(n):
    line = list(map(int, input().split()))
    linemax = max(line)
    linemin = min(line)

    if linemax > maxh:
        maxh = linemax
    if linemin < minh:
        minh = linemin
    graph.append(line)


def bfs(startx, starty, visited, height):
    global n
    visited[startx][starty] = True

    q = deque()
    q.append((startx, starty))

    while q:
        x, y = q.popleft()
        nexts = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]

        for nex in nexts:
            a = nex[0]
            b = nex[1]
            if a < 0 or b < 0 or a >= n or b >= n:
                continue
            if visited[a][b]:
                continue
            if graph[a][b] < height:
                visited[a][b] = True
                continue
            visited[a][b] = True
            q.append((a, b))


max_areas = 1
for h in range(minh + 1, maxh + 1):
    visited = [[False] * n for _ in range(n)]
    areas = 0
    for x in range(n):
        for y in range(n):
            # 방문여부 체크해야함, 높이 체크해야함
            if visited[x][y]:
                continue
            if graph[x][y] < h:
                continue
            areas += 1
            bfs(x, y, visited, h)
    if max_areas < areas:
        max_areas = areas

print(max_areas)
