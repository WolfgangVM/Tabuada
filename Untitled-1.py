from tkinter import*

# definição da janela
janela = Tk()
janela.title("Tabuada")

#interface de interação da interface

label = Label(janela, text="Qual o resultado""\n""dessa multipliucação", font=("Arial", 12))
label.grid (row=0, column=1, padx=0, pady=0)

label = Label(janela, text= "numero x numero",font=("Arial", 12), fg='green',bg='black')
label.grid (row=1, column=1, padx=5,pady=5)

botao1 = Button(janela, text="opção1")
botao1.grid(row=3, column=0)

botao2 = Button(janela, text="opção2")
botao2.grid(row=4, column=0)

botao3 = Button(janela, text="opção3")
botao3.grid(row=3, column=1)

botao4 = Button(janela, text="opção4")
botao4.grid(row=4, column=1)

acertos = Label(janela,text="Acertos:",font=("Arial",10), fg='green')
acertos.grid (row=5, column=0)

janela.mainloop()