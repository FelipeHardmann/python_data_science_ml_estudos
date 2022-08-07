def calcularImc(infos: list) -> None:
    for info in  infos:
        nome, peso, altura = info
        imc = peso / (altura ** 2)
        print(f'{nome.title()} - IMC: {round(imc, 2)}')

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