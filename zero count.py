def count(list):
    count = 0
    for item in list:
        if item == 0:
            count += 1
    return count


n = [3, 0, 5, 8, 0]
zero_count = count(n)
print(zero_count)
