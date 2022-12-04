from functools import reduce

# Questão 1
lista = [num for num in range(1, 21)]
pares = list(filter(lambda num: num % 2 == 0, lista ))

# Questão 2
lista2 = [num for num in range(30, 51)]
impares = list(filter(lambda num: num % 2 == 1, lista2))

# Questão 3
lista3 = [num for num in range(-10, 11)]
menor_0 = list(filter(lambda num: num < 0, lista3))

# Questão 4
lista4 = [num for num in range(1000)]
menor = reduce(lambda x, y: x if x < y else y, lista4)

# Questão 5
lista5 = ['maria', 'felipe', 'adriano', 'souza']
maiusculos = list(map(lambda txt: txt.title(), lista5))

# Questão 6
lista5.sort(key = lambda txt: txt[1])

# Questão 7
lista6 = lista5
lista6.sort(key = lambda txt: txt[1], reverse=True)

# Questão 8
nova_lista = list(map(lambda num: num * 10 if num % 2 == 0 else round(num / 3, 2), lista))

print(lista6)