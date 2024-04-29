from tkinter import*

janela = Tk()
janela.title("Tabuada")
janela.geometry('400x600')

label = Label(janela, text="Qual o resultado dessa multipliucação", font=("Arial", 12))
label.grid (column= 0, row = 0)
label = Label(janela, text= "numero x numero",font=("Arial", 12), fg='green',bg='black')
label.grid (column=0, row=1)

janela.mainloop()