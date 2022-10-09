from tkinter import messagebox
import mysql.connector
from tkinter import *
from cores import *

def conectar():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user=campoNome.get(),
            passwd=campoSenha.get(),
            db='INFINITY'
        )
    except:
        messagebox.showerror('Erro', 'Erro ao conecctar no Banco de dados')
    else:
        messagebox.showinfo('conectado', 'Conexão realizada com sucesso')

#Construindo minha janela
janela = Tk()
janela.title('Projeto 1')
janela.geometry('310x300')
janela.resizable(width=False, height=False)

#Dividindo em frames
frameSuperior = Frame(
    janela,
    width=310,
    height=50, 
    bg=COR_FUNDO
)
frameSuperior.grid(row=0, column=0, sticky=NSEW)

frameInferior = Frame(
    janela, 
    width=310,
    height=250,
    bg=COR_FUNDO
)
frameInferior.grid(row=1, column=0, sticky=NSEW)

#Configurando o frame superior
titulo = Label(
    frameSuperior, 
    text='Login',
    anchor=NW,
    font=('Malgun Gothic', 22),
    bg=COR_FUNDO,
    fg=COR_LETRA
)
titulo.place(x=5, y=4)

linha = Label(
    frameSuperior,
    width=275,
    anchor=NW,
    bg=COR_IN
)
linha.place(x=20, y=48)

#configurando o frame inferior
nome = Label(
    frameInferior,
    text='Nome',
    anchor=NW,
    font=('Malgun Gothic', 14),
    bg=COR_FUNDO,
    fg=COR_LETRA
)
nome.place(x=10, y=20)

campoNome = Entry(
    frameInferior,
    width=28,
    justify='left',
    font=('malgun Gothic', 14),
    highlightthickness=1,
    relief='solid'
)
campoNome.place(x=10, y=50)
campoNome.focus()

senha = Label(
    frameInferior,
    text='Senha',
    anchor=NW,
    font=('Malgun Gothic', 14),
    bg=COR_FUNDO,
    fg=COR_LETRA
)
senha.place(x=10, y=95)

campoSenha = Entry(
    frameInferior,
    width=25,
    justify='left',
    show='*',
    font=('Malgun, Gothic', 14),
    highlightthickness=1, 
    relief='solid'
)
campoSenha.place(x=10, y=130)

btnEntrar = Button(
    frameInferior,
    text='Entrar',
    font=('Malgun Gothic', 14),
    width=25,
    bg=COR_IN,
    fg=COR_FUNDO,
    command=conectar,
)
btnEntrar.place(x=10, y=180)

if __name__ == '__main__':
    janela.mainloop()