'''
Projeto de teste
'''

from tkinter import *

def saudacao(): 
    if cx_text.get() == '':
        msg['text'] = 'Olá'
    else:
        msg['text'] = f'Olá, {cx_text.get().title()}' #Função para pegar o que está digitado no Label
        cx_text.delete(0, 'end') #Função para deletar o conteúdo dentro do label


janela = Tk()

rotulo = Label(
    text='Digite seu nome: ',
    font=('Arista 2.0 Alternate', 24)
)
rotulo.grid(row=0, column=0, padx=25, pady=15)

cx_text = Entry(
    font=('Artifakt Element', 24)
)
cx_text.grid(row=0, column=1, padx=25, pady=15)
cx_text.focus()#Isso já deixa a caixa texto para o usuário ñ precisar digitar

btn = Button(
    text='Saudação',
    font=('Artifakt Element', 24),
    command=saudacao
    )
btn.grid(row=0, column=2, padx=25, pady=15, sticky=NS)

back = Button(
    text='Sair',
    font=('Artifakt Element', 24),
    command=exit #Essa função já fecha a janela
)
back.grid(row=1, column=2, padx=25, pady=15, sticky=EW)


msg = Label(
    text='----',
    font=('Birds of Paradise Personal use', 36)
)
msg.grid(row=1, column=0, columnspan=3)


if __name__ == '__main__':
    janela.mainloop()