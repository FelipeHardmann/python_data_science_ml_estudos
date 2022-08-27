class Produto:
    def __init__(self, nome, preco, categoria, descricao):
        self.nome = nome
        self.__preco = preco
        self.__categoria = categoria
        self.descricao = descricao

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        return 'Preço inválido'

    @property
    def categoria(self):
        return self.__categoria

    def aplicar_desconto(self, percentual):
        self.preco = self.preco - self.preco * (percentual / 100)

    '''def __repr__(self):
        return f'{self.nome} - {self.__categoria}'''

    '''def __str__(self):
        return f'{self.nome} - {self.descricao}'''

    if __name__ == '__main__':
        print('Rode o cadastrar produto')
