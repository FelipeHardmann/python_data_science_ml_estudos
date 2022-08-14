from typing import Union

#Caracteres
'''
Union: Biblioteca que serve para representar dois valores
'''
def cont_letras(palavra: str, conta: bool = False) -> Union[bool, int]:
    '''
    Recebe uma palavra e retorna a quantidade de letras na palavra
    '''
    cont = 0
    for _ in range(palavra):
        cont += 1

def conta_vogais(palavra: str, conta: bool = False) -> Union[bool, int]:
    '''
    Recebe uma palavra e retoorna a uantidade de vogais nela
    '''
    if palavra.count('a', 'e', 'i', 'o', 'u'):
        return Union
    else:
        return conta
    
def eh_palidromo(palavra: str) -> True:
    '''
    Recebe uma palavra e vai dizer se é palindromoo ou não
    '''
    ...

def tem_maiusculas(palavra: str, contar: bool = False) -> Union[bool, int]:
   '''
   Recebe uma palavra e vai retoorna se tem maiúsculas ou não
   '''
   number = 0
   for _ in (palavra):
        if palavra.isupper():
            number += 1
        return number

def tem_minusculas(palavra: str, contar: bool = False) -> Union[bool, int]:
    '''
    Recebe uma palavra e vai retorna se tem maiúsculas ou não
    '''
    number = 0
    for _ in range(palavra):
        if palavra.islower():
            number += 1
        return number

