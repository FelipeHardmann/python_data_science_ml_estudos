from tkinter import (
    Button,
    Tk,
    Label
)

def clicar():
    # print('Fui clicado')
    texto['text'] = 'Botão clicado'
    texto['fg'] = 'blue'
    

janela = Tk()
janela.title('IN')
texto = Label(
    text='Minha primeira janela',
    font=('Arial', 50),
    padx= 50,
    pady= 50
    )
texto.pack()

btn = Button(
    text='Clica ni mim',
    font=('Arial', 24),
    command=clicar
    )
btn.pack(pady=20)

if __name__ == '__main__':
    janela.mainloop()