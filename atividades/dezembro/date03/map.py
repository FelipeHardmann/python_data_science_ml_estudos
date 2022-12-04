# função map -> Vai mapear o interável
nomes = ['ana', 'paula', 'pedro']
print(list(map(lambda nome: nome.title(), nomes)))

numbers = [1, 2, 3, 4]
print(list(map(lambda dobro: dobro * 2, numbers)))


pessoas = [
        {
            'nome': 'Rafael',
            'idade': 46
        },
        {
            'nome': 'Gustavo',
            'idade': 25
        },
        {
            'nome': 'Willian',
            'idade': 22
        }
]

print(pessoas[1]['nome'])

# Função filter

print(list(filter(lambda menor_30: menor_30['nome'])))