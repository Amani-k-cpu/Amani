
limit = 90
pos = 0
found = False
values = [90, 80, 70, 60]
while pos < len(values) and not found:
    if values [pos] == limit:
        found = True
    else:
        pos = pos + 1
if found:
    print("the postion", pos)
else:
    ("not found")