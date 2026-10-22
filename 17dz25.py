total = 0
mn = None
mx = None
count = 0
with open("big.txt") as f:
    for line in f:
        n = int(line)
        total += n
        if mn is None or n < mn:
            mn = n
        if mx is None or n > mx:
            mx = n
        count += 1
print(total)
print(mn)
print(mx)
print(count)
print(total / count)