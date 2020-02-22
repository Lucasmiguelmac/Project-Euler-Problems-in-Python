def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    max_divisor = int(num**0.5)
    for d in range(3, max_divisor+1, 2):
        if num % d == 0:
            return False
    return True

def primeSumUpTo(num):
    sum = 0
    for i in range(num):
        if is_prime(i):
            sum += i
    return sum

print(primeSumUpTo(2000000))
