from collections import deque

n = int(input())

values = [-1] * (n + 1)


def dfs():
    global values

    start = 1
    q = deque()
    q.append(start)

    values[start] = 0

    while q:
        a = q.popleft()
        bs = [a + 1, a * 2, a * 3]
        for b in bs:
            if b > n:
                continue
            if values[b] == -1:
                values[b] = values[a] + 1
                q.append(b)

dfs()

print(values[n])
