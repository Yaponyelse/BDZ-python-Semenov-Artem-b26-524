import re
text = input()
pattern = re.compile(r"(?:\+7|8)\s*(?:\(\d{3}\)|\d{3})\s*\d{3}-\d{2}-\d{2}")
for m in pattern.finditer(text):
    print(m.group())