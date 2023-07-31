def reverse(s):
    str = " "
    for i in s:
        str = i + str
    return str

x = input("enter: ")

print(reverse(x))