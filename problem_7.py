import math

def is_prime_v3(n):
    # Return True if n is a prime number, False otherwise
    if n==1:
        return False
    if n==2:
        return True # 2 es nro primo asi que si se trata de 2 ya sabemos que es primo
    
    if n>2 and n%2 == 0:
        return False # Si es mayor a dos y es par, ése número ya no es primo porque además de ser divisible por si mismo y por uno es divisible por 2.
     
    max_divisor = math.floor(n ** 0.5)
    for d in range(3, max_divisor+1, 2): # Reducimos la cantidad de valores a chequear eliminando los números pares diferentes a 2
        if n % d == 0:
            return False
    return True

prime_lst = [2, 3]
num = 3
while len(prime_lst) < 10001:
    num += 1
    if is_prime_v3(num):
        prime_lst.append(num)
print(prime_lst[-1])
