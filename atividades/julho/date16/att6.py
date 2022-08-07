n = int(input('Digite um número para calcular o fatorial: '))
result = 1

print(f'{n}! = ', end=' ')
for num in range(n, 0, -1):
    result *= num  
    if num == 1:    
        print(f'{num}', end=' ')
    else:
        print(f'{num} x', end=' ')
else:
    print(f'= {result}')      
    