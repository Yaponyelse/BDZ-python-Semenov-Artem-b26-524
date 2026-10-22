lines = 0
words = 0
chars = 0
max_len = 0
with open("file.txt") as file:
    for line in file:
        lines += 1
        chars += len(line)
        stripped = line.rstrip("\n").rstrip("\r")
        if len(stripped) > max_len:
            max_len = len(stripped)
        words += len(line.split())
print(lines)
print(words)
print(chars)
print(max_len)