numeros = [num for num in range(21)]

par = list(filter(lambda num: num % 2 == 0, numeros))
# print(par)

impar = list(filter(lambda num: num % 2 == 1, numeros))
# print(impar)

teste = list(map(lambda num: num + 10 if num % 2 == 0 else round(num / 2, 2), numeros))
# print(teste)

teste2 = list(map(lambda num: num if num > 10 else None, numeros))
print(teste2)

teste3 = list(filter(lambda num: num > 10, numeros))
print(teste3)