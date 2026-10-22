def parse_number(value):
    return int(value)
value = input()
try:
    print(parse_number(value))
except ValueError:
    print("not a number")