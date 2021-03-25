from tkinter import *
import pandas as pd
import sqlite3

janela = Tk()


class Janelas():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frame_tela()
        self.menus()
        janela.mainloop()


    def tela(self):
        self.janela.title('Janela Consulta')
        self.janela.geometry("1350x700+5+5")
        
        self.janela.configure(background='black')

    def frame_tela(self):
        self.frame_dados = Frame(self.janela)
        self.frame_dados.place(relx=0.009, rely=0.01, relwidth=0.985, relheight=0.3)
        self.frame_dados2 = Frame(self.janela)
        self.frame_dados2.place(relx=0.009, rely=0.32, relwidth=0.985, relheight=0.65)

    
    def semComando():
        print('')
    
    
    
    def menus(self):
        self.barraDeMenus = Menu(self.janela )
        self.menuContatos = Menu(self.barraDeMenus, tearoff=0)
        self.menuContatos.add_command(label='NOVO', command=self.semComando)
        self.menuContatos.add_command(label='PESQUISAR', command=self.semComando)
        self.menuContatos.add_command(label='DELETAR', command=self.semComando)
        self.menuContatos.add_separator()
        self.menuContatos.add_command(label='FECHAR', command=self.semComando)
        self.barraDeMenus.add_cascade(label='Contatos', menu=self.menuContatos)
        self.janela.config(menu=self.barraDeMenus)


    def preencher(self):
        #=============== CRIANDO ENTRY ====================================

        self.edit_inicial = Entry(self.janela)
        self.edit_idade = Entry(self.janela)
        self.edit_telefone = Entry(self.janela)
        self.edit_data = Entry(self.janela)
        self.edit_hipotese = Entry(self.janela)
        self.edit_outros = Text(self.janela)
        self.edit_primeiro = Text(self.janela)

        #=============== CRIANDO LABEL ====================================

        self.lcadastro = Label(self.janela, text='CADASTRO DE CLIENTES')
        self.label_inicial = Label( self.janela, textvariable=final)
        self.lidade = Label(self.janela, text='IDADE')
        self.ldata_inicio = Label(self.janela, text='DATA DE INICIO' )
        self.ltelefone = Label(self.janela, text='TELEFONE')
        self.lhipotese = Label(self.janela, text='HIPÓTESE DIAGNÓSTICA')
        self.lprimeiro = Label(self.janela, text='PRIMEIRO ATENDIMENTO')
        self.loutros = Label(self.janela, text='OUTROS ATENDIMENTOS')

        # ================================ CRIANDO BOTÃO ===========================

        self.botao_inicial = Button(self.janela, text='Salvar', command=self.semComando)
        self.botao_mostrar = Button(self.janela, text='Mostrar', command=self.semComando)

        



Janelas()
