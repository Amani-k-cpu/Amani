def num_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+ 1):
        if num % i ==0:
            return False
    return True

for num in range(1, 31):
        print(num, num_prime(num))
       