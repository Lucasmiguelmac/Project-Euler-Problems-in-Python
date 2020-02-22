def EvenlyDividedByUpTo(num, top):
    for i in range(1, top+1):
        if num % i != 0:
            return False
    return True

# EvenlyDividedByUpTo(2520, 10)

def SmallestNumberEvenlyDividedByUpTo(top):
    num = top
    while not EvenlyDividedByUpTo(num, top):
        num += 20
    return num

SmallestNumberEvenlyDividedByUpTo(20)
