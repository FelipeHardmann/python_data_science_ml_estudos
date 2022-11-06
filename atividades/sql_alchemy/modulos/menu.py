'''Este é o modulo de menu'''

import os
import platform

def limpaTela() -> None:
    '''
    Limpa a tela do terminal

    return:
        None
    '''
    if platform.system() == 'Windowns':
        os.system('cls')
    else:
        os.system('Clear')

def cabecalho(txt: str) -> str:
    return f'{txt:-^50}'

def menu_principal() -> int:
    '''
    Exibe o menu principal na tela

    return:
        
    '''