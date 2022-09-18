import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
ralo = list(map(int, input().split()))

count = 0
for i in range(n-1):
    other = list(map(int, input().split()))
    gapsum = 0
    for j in range(m):
        gap = abs(ralo[j] - other[j])
        gapsum += gap
    if gapsum > 2000:
        count += 1
if n // 2 <= count:
    print("YES")
else:
    print("NO")
