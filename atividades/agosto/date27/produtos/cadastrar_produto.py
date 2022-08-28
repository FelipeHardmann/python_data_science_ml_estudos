from produto import Produto

listas_produtos = []

while True:
    produto1 = Produto(
        input('Produto: '),
        float(input('Preço: ')),
        input('Categoria: '),
        input('Descrição: ')
    )
    listas_produtos.append(produto1)
    if input('Deseja continuar? (N ou n)') in 'Nn':
        break

   

for prod in listas_produtos:
    print('-' * 20)
    print(
        prod.nome,
        prod.preco,
        prod.categoria,
        prod.descricao,
        sep='\n'
    )