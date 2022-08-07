#Refatoramento

def calcularImc(peso: float, altura: float) -> float:
        imc = peso / (altura ** 2)
        print(f'IMC: {round(imc, 2)}')

nomes = []
pesos = []
alturas = []

for _ in range(4):
    nome: str = input('Nome: ')
    peso: float = float(input('Peso: '))
    altura: float = float(input('Altura: '))
    nomes.append(nome)
    pesos.append(peso)
    alturas.append(altura)

dados = list(zip(nomes, pesos, alturas))

for dado in dados:
    nome, peso, altura = dado
    imc_calculado = calcularImc(peso, altura)
    print(f'{nome.title()} - IMC {imc_calculado}')