n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2

for i in range(1, n+1):
    if i+2 > n:
        break
    dp[i+2] = dp[i] + dp[i+1]


print(dp[n] % 10007)