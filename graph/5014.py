from collections import deque

h, start, target, up, down = list(map(int, input().split()))

counts = [-1] * (h + 1)


def isvalid(i):
    return 0 < i <= h


def bfs():
    global h, start, target, up, down
    q = deque()

    q.append(start)
    counts[start] = 0

    approached = False
    while q and not approached:
        now = q.popleft()
        nexts = [now+up, now-down]
        for nex in nexts:
            if isvalid(nex) and counts[nex] == -1:
                counts[nex] = counts[now] + 1
                if nex == target:
                    approached = True
                    break
                else:
                    q.append(nex)


bfs()

if counts[target] == -1:
    print("use the stairs")
else:
    print(counts[target])