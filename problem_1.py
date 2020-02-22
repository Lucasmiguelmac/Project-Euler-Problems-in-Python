def m3or5(top):
    sum = 0
    for i in range(1, (top)):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum

print(m3or5(1000))
