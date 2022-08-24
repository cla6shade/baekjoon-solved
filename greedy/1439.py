s = input()

zeros = 0
ones = 0
before = "-1"
for i in range(0, len(s)):
    if before == "-1":
        # 처음인 경우
        before = s[i]
        if s[i] == "0":
            zeros += 1
        else:
            ones +=1
        continue
    # 2번째 이상
    if before == s[i]:
        continue
    else:
        before = s[i]
        if s[i] == "0":
            zeros += 1
        else:
            ones +=1
if zeros > ones:
    print(ones)
else:
    print(zeros)