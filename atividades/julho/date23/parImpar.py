lista = []
pares = 1
impares = 1

for i in range(10):
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'A uantidade de números pares são {pares}')
print(f'A uantidade de números pares são {impares}')