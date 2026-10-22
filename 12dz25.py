import re
text = """Контакты:
alice@example.com
bob@test.org
alice@example.com
admin@company.ru"""
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
seen = set()
for e in emails:
    if e not in seen:
        seen.add(e)
        print(e)