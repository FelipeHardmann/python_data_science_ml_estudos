from produto import Produto

listas_produtos = []

while True:
    produto1 = Produto(
        input('Produto: '),
        float(input('Preço: ')),
        input('Categoria: '),
        input('Descrição: ')
    )

    if input('Deseja continuar? (N ou n)') in 'Nn':
        break

    listas_produtos.append(produto1)

for prod in listas_produtos:
    print('-' * 20)
    print(
        
    )