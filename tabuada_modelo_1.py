import random
import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Conectar ao banco de dados
conexao_bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Tabuada"
)

# Função para criar a tabela de ranking se não existir
def criar_tabela_ranking():
    cursor = conexao_bd.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS ranking (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(50),
                        pontos INT
                    )""")
    conexao_bd.commit()
    cursor.close()

# Função para inserir pontuação no ranking
def inserir_pontuacao(nome, pontos):
    cursor = conexao_bd.cursor()
    cursor.execute("INSERT INTO ranking (nome, pontos) VALUES (%s, %s)", (nome, pontos))
    conexao_bd.commit()
    cursor.close()

# Função para mostrar o ranking em uma janela Tkinter
def mostrar_ranking_tk():
    cursor = conexao_bd.cursor()
    cursor.execute("SELECT nome, pontos FROM ranking ORDER BY pontos DESC LIMIT 10")
    ranking = cursor.fetchall()

    # Criar janela Tkinter para mostrar o ranking
    ranking_window = tk.Tk()
    ranking_window.title("Ranking")
    ranking_window.geometry("300x200")

    # Criar e exibir o ranking na janela
    ranking_label = tk.Label(ranking_window, text="Ranking:")
    ranking_label.pack()

    for posicao, (nome, pontos) in enumerate(ranking, start=1):
        posicao_label = tk.Label(ranking_window, text=f"{posicao}. {nome}: {pontos} pontos")
        posicao_label.pack()

    ranking_window.mainloop()

# Função principal do jogo
def jogo_tabuada():
    nome_jogador = input("Digite seu nome: ")

    pontuacao = 0
    for _ in range(10):  # 10 perguntas
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        resposta_correta = num1 * num2

        # Criar janela Tkinter para exibir a pergunta
        pergunta_window = tk.Tk()
        pergunta_window.title("Pergunta de Tabuada")
        pergunta_window.geometry("200x150")

        pergunta_label = tk.Label(pergunta_window, text=f"Quanto é {num1} * {num2}?")
        pergunta_label.pack()

        resposta_entry = tk.Entry(pergunta_window)
        resposta_entry.pack()

        def verificar_resposta():
            resposta_jogador = resposta_entry.get()
            try:
                resposta_jogador = int(resposta_jogador)
                if resposta_jogador == resposta_correta:
                    messagebox.showinfo("Resposta Correta!", "Resposta correta!")
                    nonlocal pontuacao
                    pontuacao += 10
                else:
                    messagebox.showinfo("Resposta Incorreta!", f"Resposta incorreta! A resposta correta era {resposta_correta}")
            except ValueError:
                messagebox.showwarning("Entrada Inválida!", "Por favor, digite um número válido.")

            pergunta_window.destroy()

        verificar_button = tk.Button(pergunta_window, text="Verificar", command=verificar_resposta)
        verificar_button.pack()

        pergunta_window.mainloop()

    messagebox.showinfo("Fim do Jogo", f"Fim do jogo! Sua pontuação: {pontuacao} pontos")

    inserir_pontuacao(nome_jogador, pontuacao)
    mostrar_ranking_tk()

# Criar tabela de ranking se não existir
criar_tabela_ranking()

# Execução do jogo
jogo_tabuada()

# Fechar conexão com o banco de dados no final do programa
conexao_bd.close()
