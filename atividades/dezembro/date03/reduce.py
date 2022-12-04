# Reduce -> Sempre dois parametros
from functools import reduce

numeros = [12, 43, 3224, 4, 123, 483, 999, 13, 44, 1000]
mult = reduce(lambda x, y: x * y, numeros)
soma = reduce(lambda x, y: x + y, numeros)

print(f'A multiplicação da lista é: {mult} e a Soma: {soma}')