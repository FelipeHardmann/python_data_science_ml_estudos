
'''
Aqui fica uma explicaçãoo soobre oo moodulo e suas funções
'''

def par_ou_impar(numero: int) -> str:#Assinatura de função
    '''
    Recebe dois números inteiros e retorna se é par ou ímpar
    '''
    if numero % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'

def calcula_percentual(numero1: float, numero2: float) -> float:
    '''
    Recebe um número e uma porcentagem e calcula a sua porcentagem
    '''
    percentual = numero1 / numero2
    return percentual
    
def divide_dois(numero1: float, numero2: float) -> float:
    '''
    Recebe dois números para de dividir um pelo outro
    '''
    return numero1 / numero2

def fatorial(numero: int) -> int:
    '''
    Recebe um número e multiplica o ele pelo antecessor
    Ex:
    5!
    5 X 4 X 3 X 2 X 1 = 120
    '''
    resultado = 1
    count = 1
    while count <= numero:
        resultado *= count
        count += 1  
    return resultado
    
def media(numero1: float) -> list:
    '''
    Recebe dois ou mais números, faz a soma entre eles e divide 
    pela quantidade de números
    '''
    
def multiplica_dois(numero1: float, numero2: float) -> float:
    '''
    Recebe dois números e multiplica um pelo outro
    '''
    return numero1 * numero2

def potencia(numero1: int, numero2: int) -> int:
    '''
    Recebe dois números um como base e outro como potência
    '''
    return numero1 ** numero2

def quantos_porcento(numero1: int, numero2: float) -> int:
    '''
    Recebe um número 
    '''
    porcentagem = numero2 / 100
    numero1 = numero1 * porcentagem

    return numero1, porcentagem
    
def soma_dois(numero1: int, numero2: int) -> int:
    '''
    Recebe dois números e somam eles
    '''
    return numero1 + numero2

def subtrai_dois(numero1: int, numero2: int) -> int:
    '''
    Recebe dois números e subtrai um pelo outro
    '''
    return numero1 - numero2

print(fatorial(5))
print(par_ou_impar(10))
    