#tkinter (tk): Biblioteca para criar interfaces gráficas (GUI) em Python
import tkinter as tk 
#ttk: Módulo do tkinter que fornece widgets com visual mais moderno
from tkinter import ttk
#pandas (pd): Biblioteca para manipulação e análise de dados
import pandas as pd
#deque: Estrutura de dados do tipo fila dupla (double-ended queue) otimizada
from collections import deque

class PrincipalFila:
    def __init__(self, win):
        self.fila = deque()  #Criando a fila para armazenar os alunos

        #Labels
        self.lblNome = tk.Label(win, text='Nome:')
        self.lblNota1 = tk.Label(win, text='Nota 1:')
        self.lblNota2 = tk.Label(win, text='Nota 2:')

        #Entradas
        self.txtNome = tk.Entry()
        self.txtNota1 = tk.Entry()
        self.txtNota2 = tk.Entry()

        #Botões
        self.btnAdicionar = tk.Button(win, text='Adicionar à Fila', command=self.adicionarNaFila)
        self.btnProcessar = tk.Button(win, text='Processar Primeiro', command=self.processarFila)

        #TreeView
        self.treeFrame = tk.Frame(win)
        self.treeFrame.place(x=100, y=200, width=700, height=200)
        
        self.dadosColunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")
        self.treeMedias = ttk.Treeview(self.treeFrame, columns=self.dadosColunas, show="headings")
        self.treeMedias.pack(side="left", fill="both", expand=True)
        
        self.verscrlbar = ttk.Scrollbar(self.treeFrame, orient="vertical", command=self.treeMedias.yview)
        self.verscrlbar.pack(side="right", fill="y")
        self.treeMedias.configure(yscrollcommand=self.verscrlbar.set)
        
        for col in self.dadosColunas:
            self.treeMedias.heading(col, text=col)
            self.treeMedias.column(col, width=100)
        
        #Posicionamento
        self.lblNome.place(x=100, y=40)
        self.txtNome.place(x=150, y=40)
        self.lblNota1.place(x=100, y=70)
        self.txtNota1.place(x=150, y=70)
        self.lblNota2.place(x=100, y=100)
        self.txtNota2.place(x=150, y=100)
        
        self.btnAdicionar.place(x=100, y=150)
        self.btnProcessar.place(x=250, y=150)
    
    def adicionarNaFila(self):
        try:
            nome = self.txtNome.get()
            nota1 = float(self.txtNota1.get())
            nota2 = float(self.txtNota2.get())
            self.fila.append((nome, nota1, nota2))
            print(f"{nome} adicionado à fila.")
            
            self.txtNome.delete(0, 'end')
            self.txtNota1.delete(0, 'end')
            self.txtNota2.delete(0, 'end')
        except ValueError:
            print("Entre com valores válidos!")
    
    # Esse método é responsável por adicionar um aluno e suas notas na fila de processamento
    # Ele:
    # 1. Obtém o nome e notas digitados nos campos de texto (txtNome, txtNota1, txtNota2)
    # 2. Converte as notas para números (float)
    # 3. Adiciona uma tupla (nome, nota1, nota2) na fila
    # 4. Limpa os campos de texto após adicionar
    # 5. Trata erros de conversão caso o usuário digite valores inválidos
  
    def processarFila(self):
        if self.fila:
            nome, nota1, nota2 = self.fila.popleft()
            media, situacao = self.verificarSituacao(nota1, nota2)
            self.treeMedias.insert('', 'end', values=(nome, nota1, nota2, media, situacao))
            print(f"{nome} processado.")
        else:
            print("A fila está vazia!")

    # Esse código é um sistema de gerenciamento de notas de alunos usando uma interface gráfica Tkinter
    # Ele permite:
    # - Adicionar alunos com suas notas em uma fila
    # - Processar a fila mostrando a média e situação de cada aluno
    # - Exibir os resultados em uma tabela (TreeView)
    # 
    # A fila é usada para armazenar temporariamente os dados dos alunos (nome e notas)
    # antes de serem processados e exibidos na tabela
    # 
    # O método verificarSituacao calcula a média e determina se o aluno está:
    # - Aprovado (média >= 7.0)
    # - Em Recuperação (média >= 5.0 e < 7.0) 
    # - Reprovado (média < 5.0)
  
    def verificarSituacao(self, nota1, nota2):
        media = (nota1 + nota2) / 2
        if media >= 7.0:
            return media, 'Aprovado'
        elif media >= 5.0:
            return media, 'Em Recuperação'
        else:
            return media, 'Reprovado'

#Programa Principal
janela = tk.Tk()
principal = PrincipalFila(janela)
janela.title('Portal de Notas - Fila')
janela.geometry("880x480+10+10")
janela.mainloop()
