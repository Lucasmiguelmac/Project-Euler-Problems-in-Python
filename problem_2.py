# Defino una lista con los valores de la sucesión de fibonacci
fib_list = [1, 2]
while fib_list[-1] <= 4000000:
    new_fib = fib_list[-1] + fib_list[-2]
    fib_list.append(new_fib)

# Defino la suma de los números pares
evensum = 0
for num in fib_list:
    if num % 2 == 0:
        evensum += num
print(evensum)
