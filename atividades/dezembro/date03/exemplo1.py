"""func_soma = lambda x, y: x + y
print(func_soma(3, 4))"""

'''func_soma = lambda *args: sum(*args)
print(func_soma([100, 100, 100, 100]))'''

nomes = ['Davi', 'Pedro', 'Lucas']
reverse = nomes.sort(key = lambda txt: txt[1], reverse=True)
print(reverse)

add_nome = lambda nome: nomes.append('Ana')
print(nomes)