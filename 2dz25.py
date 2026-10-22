mn = None
mx = None
total = 0
count = 0
with open("numbers.txt") as f:
    for line in f:
        try:
            n = int(line)
        except ValueError:
            continue
        if mn is None or n < mn:
            mn = n
        if mx is None or n > mx:
            mx = n
        total += n
        count += 1
with open("result.txt", "w") as f:
    f.write(f"{mn}\n{mx}\n{total / count}\n")