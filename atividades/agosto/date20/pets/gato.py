class Gato:
    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor

    def miar(self):
        return 'Miauuu'

    def andar(self):
        return 'andando'

    def fazerFesta(self, humor = not 0):
        return f'O cachorro está feliz {humor}'
        
        