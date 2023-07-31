def find(list, n):
    longer = [word for word in list if len(word) > n]
    return longer

user = ['Amani', 'Eman', 'alaa', 'r']
n = int(input("Enter the minimum length of words: "))

result = find(user, n)
print("Words longer than", n, "characters:", result)