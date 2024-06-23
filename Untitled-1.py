from tkinter import Tk, Label, Button
import random

# Definição da janela principal da aplicação
janela = Tk()
janela.title("Tabuada")

# Variáveis globais
acertos_contador = 0
questoes_contador = 0
total_questoes = 10  # Limite de questões

# Label inicial que apresenta a pergunta sobre a multiplicação
label = Label(janela, text="Qual é o resultado desta multiplicação?", font=("Arial", 12))
label.grid(row=0, column=1, padx=10, pady=10)

# Label que mostra a quantidade de acertos
acertos_label = Label(janela, text="Acertos: 0", font=("Arial", 10), fg='green')
acertos_label.grid(row=5, column=1)

# Função para gerar uma nova pergunta de tabuada
def tabuada():
    global num1, num2, res_correta, questoes_contador
    if questoes_contador >= total_questoes:
        mostrar_resultado()
        return
    
    # Gera dois números aleatórios entre 1 e 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    res_correta = num1 * num2

    # Atualiza o label com a nova pergunta
    pergunta_label.config(text=f"{num1} x {num2} = ?")

    # Gera uma lista de respostas com a correta e algumas incorretas
    respostas = [res_correta, res_correta + random.randint(1, 10), res_correta - random.randint(1, 10), res_correta + random.randint(11, 20)]
    random.shuffle(respostas)  # Embaralha a lista de respostas

    # Atualiza os textos dos botões com as respostas embaralhadas e associa a função de verificação a cada botão
    botao1.config(text=respostas[0], command=lambda r=respostas[0]: verificar_resposta(r))
    botao2.config(text=respostas[1], command=lambda r=respostas[1]: verificar_resposta(r))
    botao3.config(text=respostas[2], command=lambda r=respostas[2]: verificar_resposta(r))
    botao4.config(text=respostas[3], command=lambda r=respostas[3]: verificar_resposta(r))
    
    questoes_contador += 1

# Função para verificar se a resposta selecionada é correta
def verificar_resposta(resposta):
    global acertos_contador
    if resposta == res_correta:
        acertos_contador += 1  # Incrementa o contador de acertos se a resposta estiver correta
        acertos_label.config(text=f"Acertos: {acertos_contador}")  # Atualiza o label de acertos
    tabuada()  # Gera uma nova pergunta independentemente se a resposta estava correta ou não

# Função para mostrar o resultado final após as 10 questões
def mostrar_resultado():
    pergunta_label.config(text=f"Você acertou {acertos_contador} de {total_questoes} questões!")
    botao1.grid_remove()
    botao2.grid_remove()
    botao3.grid_remove()
    botao4.grid_remove()

# Função para iniciar o quiz, escondendo o botão de iniciar
def iniciar_quiz():
    botao_iniciar.grid_remove()  # Remove o botão de iniciar
    tabuada()  # Gera a primeira pergunta

# Label que será atualizado com a pergunta de multiplicação
pergunta_label = Label(janela, text="", font=("Arial", 12))
pergunta_label.grid(row=1, column=1, padx=10, pady=10)

# Botões de resposta que serão atualizados com as respostas possíveis
botao1 = Button(janela, text=" %s ", command=lambda: None)
botao1.grid(row=3, column=0)

botao2 = Button(janela, text=" %s ", command=lambda: None)
botao2.grid(row=4, column=0)

botao3 = Button(janela, text=" %s ", command=lambda: None)
botao3.grid(row=3, column=1)

botao4 = Button(janela, text=" %s ", command=lambda: None)
botao4.grid(row=4, column=1)

# Botão para iniciar a tabuada, que chama a função iniciar_quiz ao ser clicado
botao_iniciar = Button(janela, text="Iniciar Tabuada", command=iniciar_quiz)
botao_iniciar.grid(row=6, column=1)

# Inicia o loop principal da aplicação
janela.mainloop()
