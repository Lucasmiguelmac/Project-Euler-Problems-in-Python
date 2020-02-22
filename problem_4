def is_palindrome(num):
    strn = str(num)
    if strn[0] == strn[-1]:
        if strn[1] == strn[-2]:
            if strn[2] == strn[-3]:
                return True
    
palindrome_lst = []
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product):
            palindrome_lst.append(product)
            
print(max(palindrome_lst))
