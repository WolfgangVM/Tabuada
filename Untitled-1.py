from tkinter import*

# definição da janela
janela = Tk()
janela.title("Tabuada")
janela.geometry('400x600')

#interface de interação da interface
label = Label(janela, text="Qual o resultado dessa multipliucação", font=("Arial", 12))
label.grid (column= 0, row = 0)

label = Label(janela, text= "numero x numero",font=("Arial", 12), fg='green',bg='black')
label.grid (column=0, row=1)

label = Label(janela, text="")# deixa uma linha de espaço
label.grid(column=0, row=2)

botao1 = Button(janela, text="opção1")
botao1.grid(column=0, row=3)

botao2 = Button(janela, text="opção2")
botao2.grid(column=0, row=4)

botao3 = Button(janela, text="opção3")
botao3.grid(column=1, row=3)

botao4 = Button(janela, text="opção4")
botao4.grid(column=1, row=4)

janela.mainloop()