'''class Aluno:

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email'''

"""from random import randint

def gera_numero_conta(tamanho: int) -> int:
    '''
    Gera valor aleatório para se criar um número de conta
    '''
    return int(''.join([ str(randint(0, 9)) for _ in range(tamanho)]))"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco
    
    @property
    def preco(self):
        return self.preco
    
    @preco.setter
    def preco(self, novo_valor):
        if novo_valor > 0:
            self.__preco = novo_valor
        return self.preco

    def reajustar(self, percentual):
        percetual = 1 + percentual / 100
        self.preco = percentual

    def __repr__(self):
        return self.nome

if __name__ == '__main__':
    print('Não me execute')