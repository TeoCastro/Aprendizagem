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
        self.preencher()
        self.mostrar()
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

        self.edit_inicial = Entry(self.frame_dados2)
        self.edit_idade = Entry(self.frame_dados2)
        self.edit_telefone = Entry(self.frame_dados2)
        self.edit_data = Entry(self.frame_dados2)
        self.edit_hipotese = Entry(self.frame_dados2)
        self.edit_outros = Text(self.frame_dados2)
        self.edit_primeiro = Text(self.frame_dados2)

        #=============== CRIANDO LABEL ====================================

        self.lcadastro = Label(self.frame_dados2, text='CADASTRO DE CLIENTES')
        self.label_inicial = Label( self.frame_dados2, text='NOME')
        self.lidade = Label(self.frame_dados2, text='IDADE')
        self.ldata_inicio = Label(self.frame_dados2, text='DATA DE INICIO' )
        self.ltelefone = Label(self.frame_dados2, text='TELEFONE')
        self.lhipotese = Label(self.frame_dados2, text='HIPÓTESE DIAGNÓSTICA')
        self.lprimeiro = Label(self.frame_dados2, text='PRIMEIRO ATENDIMENTO')
        self.loutros = Label(self.frame_dados2, text='OUTROS ATENDIMENTOS')

        # ======================= CRIANDO BOTÃO ===========================

        self.botao_inicial = Button(self.janela, text='Salvar', command=self.semComando)
        self.botao_mostrar = Button(self.janela, text='Mostrar', command=self.semComando)

        

    def mostrar(self):
        # =============== MOSTRANDO CAIXA DE TEXTO E BOTÃO ================

        self.botao_mostrar.place(x=750, y=650, width=70, height=20)
        self.botao_inicial.place(x=550, y=650, width=70, height=20)
        self.edit_inicial.place(x=40, y=70, width=400)
        self.edit_idade.place(x=500, y=70, width=30)
        self.edit_hipotese.place(x=180, y=145, width=930)
        self.edit_primeiro.place(x=20, y=190, width=1280, height=100)
        self.edit_outros.place(x=20, y=320, width=1280, height=100)
        self.edit_data.place(x=933, y=70)
        self.edit_telefone.place(x=717, y=70)

        # ============================================== MOSTRANDO LABEL =====================================================
        self.lcadastro.place(x=550, y=20)
        self.label_inicial.place(x=19, y=45)
        self.lidade.place(x=530, y=45)
        self.ldata_inicio.place(x=930, y=45)
        self.ltelefone.place(x=710, y=45)
        self.lhipotese.place(x=550, y=120)
        self.lprimeiro.place(x=19, y=165)
        self.loutros.place(x=19, y=295)



Janelas()
