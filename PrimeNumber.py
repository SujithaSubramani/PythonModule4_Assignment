def is_prime_while_loop(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
# Test the function
num = 70
if is_prime_while_loop(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")