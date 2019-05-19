N = int(input())

for i in range(1, N+1):
    add_zeros = False
    value = input()
    value1 = []
    value2 = []
    
    digit2 = None
    
    for digit in value:
        if digit == '4':
            digit1 = digit2 = '2'
            add_zeros = True
        else:
            digit1 = digit
            if add_zeros:
                digit2 = '0'
        
        value1.append(digit1)
        if digit2:
            value2.append(digit2)
        digit2 = None
    print("Case #{i}: {val1} {val2}".format(i=i, val1=''.join(value1), val2=''.join(value2)))

