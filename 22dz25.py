import re
text = """Полезные сайты: https://python.org, http://example.com/page,
https://example.com/docs/index.html и ftp://files.example.com/data."""
for m in re.finditer(r"https?://[^\s,]+", text):
    print(m.group())