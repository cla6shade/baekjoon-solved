n = int(input())
meetings = []
for i in range(0, n):
    a = list(map(int, input().split()))
    meetings.append((a[0], a[1]))

meetings.sort(key=lambda e: (e[0], e[1]))
print(meetings)
