def lpf(num):
    # Encuentro lo números divisores del número
    divisors_lst = []
    for divisor in range(1, num+1):
        if num % divisor == 0:
            divisors_lst.append(divisor)
    
    # De los números divisores que encontré me fijo cuáles son primos
    prime_divisors_lst = []
    for i in divisors_lst:
        divisor_divisors_lst = []
        for j in range(1, (i+1)):
            if i % j == 0:
                divisor_divisors_lst.append(j)
        if len(divisor_divisors_lst) <= 2:
            prime_divisors_lst.append(i)
    
    # Devuelvo el último de la lista
    return prime_divisors_lst[-1]

lpf(13195)
