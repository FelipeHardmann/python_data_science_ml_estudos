def adicao(numero1: int, numero2: int) -> int:
    return numero1 + numero2
def subt(numero1: int, numero2: int) -> int:
    return numero1 + numero2
def multi(numero1: int, numero2: int) -> int:
    return numero1 + numero2
def divisao(numero1: int, numero2: int) -> int:
    return numero1 + numero2 


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
escolhaTipo = input('Digite qual tipo de aplicação você quer fazer: (+, -, * ou /): ')

if escolhaTipo == '+':
    print(adicao)
elif escolhaTipo == '-':
    print(subt)
elif escolhaTipo == '*':
    print(multi)
elif escolhaTipo == '/':
    print(divisao)