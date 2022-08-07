n = int(input('Digite um número para calcular o fatorial: '))
cont = 0
result = 1

'''while cont > 0:
    print(f'{cont} * ', end='')
    result *= cont
    cont -= 1
print(f'O fatorial de {n} é {result}')'''


for num in range(n, 0, -1):
    result *= num    
print(result)