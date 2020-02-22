def sumOfSquaresOfUpTo(num):
    sum = 0
    for i in range(1, num+1):
        sum += i**2
    return sum

def squareOfSumUpTo(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum**2


def sumSquareDifference(num):
    result = squareOfSumUpTo(num) - sumOfSquaresOfUpTo(num)
    return result

sumSquareDifference(100)
