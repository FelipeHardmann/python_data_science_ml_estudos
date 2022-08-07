fib = int(input('Digite o tamanho da série de Fibonacci: '))
cont1 = 0
cont2 = 1
cont = 0

if fib < 2:
    for i in range(fib, 1):
        cont = cont1 + cont2
        cont1 += cont1
        cont2 += cont2
    else:
        print(f'{cont1} {cont2} {cont}')   
