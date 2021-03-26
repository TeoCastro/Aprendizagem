from tkinter import *
from tkinter import ttk
import pandas as pd
import sqlite3

janela = Tk()


class Funçoes():
    def conecta_banco(self):
        self.banco = sqlite3.connect('Banco_Clientes.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS clientes (NOME text CHAR(50) NOT NULL, IDADE integer, DATA date, TELEFONE text, HIPOTESE text, PRIMEIRO text, OUTROS text)")

        self.banco.commit()


    def desconecta_banco(self):
        self.banco.close()


    def inser(self):
        self.inicial1 = self.edit_inicial.get()
        
        self.primeiro1 = self.edit_primeiro.get("1.0", 'end')
        self.idade1 = self.edit_idade.get()
        self.dataInicio = self.edit_data.get()
        self.telefone1 = self.edit_telefone.get()
        self.hipotese1 = self.edit_hipotese.get()
        self.outros1 = self.edit_outros.get("1.0", 'end')

        cursor.execute('INSERT INTO clientes(NOME,IDADE,DATA,TELEFONE, HIPOTESE,PRIMEIRO,OUTROS)VALUES(?,?,?,?,?,?,?)',
        (self.inicial1,self.idade1,self.dataInicio,self.telefone1,self.hipotese1,self.primeiro1,self.outros1))

        self.banco.commit()
        self.select_lista()

    def select_lista(self):
        self.lista.delete(*self.lista.get_children())
        lista1 = self.cursor.execute('''SELECT NOME, IDADE, DATA, TELEFONE FROM clientes''')

        for i in lista1:
            self.lista.insert('',END,values=1)
        




class Janelas(Funçoes):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frame_tela()
        self.menus()
        self.preencher()
        self.mostrar()
        self.lista_frame()
        self.conecta_banco()
        self.select_lista()
        janela.mainloop()


    def tela(self):
        self.janela.title('Janela Consulta')
        self.janela.geometry("1350x700+5+5")
        
        self.janela.configure(background='black')

    def frame_tela(self):
        self.frame_dados = Frame(self.janela)
        self.frame_dados.place(relx=0.009, rely=0.01, relwidth=0.985, relheight=0.3)
        self.frame_dados.configure(background='brown')
        self.frame_dados2 = Frame(self.janela)
        self.frame_dados2.place(relx=0.009, rely=0.32, relwidth=0.985, relheight=0.65)
        self.frame_dados2.configure(background='brown')

    
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

        self.lcadastro = Label(self.frame_dados2,bg="#808000",font=('white',16,'bold'), text='CADASTRO DE CLIENTES')
        self.label_inicial = Label( self.frame_dados2,font=('blak',11,'bold'),bg='brown', text='NOME')
        self.lidade = Label(self.frame_dados2,font=('blak',11,'bold'),bg='brown', text='IDADE')
        self.ldata_inicio = Label(self.frame_dados2,font=('blak',11,'bold'),bg='brown', text='DATA DE INICIO' )
        self.ltelefone = Label(self.frame_dados2,font=('blak',11,'bold'),bg='brown', text='TELEFONE')
        self.lhipotese = Label(self.frame_dados2,font=('blak',11,'bold'),bg='brown', text='HIPÓTESE DIAGNÓSTICA')
        self.lprimeiro = Label(self.frame_dados2,font=('blak',11,'bold'),bg='brown', text='PRIMEIRO ATENDIMENTO')
        self.loutros = Label(self.frame_dados2,font=('blak',11,'bold'),bg='brown', text='OUTROS ATENDIMENTOS')

        # ======================= CRIANDO BOTÃO ===========================

        self.botao_inicial = Button(self.janela, text='Salvar',bd=4, command=self.inser)
        self.botao_mostrar = Button(self.janela, text='Mostrar',bd=4, command=self.semComando)

        

    def mostrar(self):
        # =============== MOSTRANDO CAIXA DE TEXTO E BOTÃO ================

        self.botao_mostrar.place(relx=0.59, rely=0.925, relwidth=0.05, relheight=0.03)
        self.botao_inicial.place(relx=0.35, rely=0.925, relwidth=0.05, relheight=0.03)
        self.edit_inicial.place(relx=0.03, rely=0.18, relwidth=0.3)
        self.edit_idade.place(relx=0.375, rely=0.18, relwidth=0.1)
        self.edit_hipotese.place(relx=0.15, rely=0.3, relwidth=0.70)
        self.edit_primeiro.place(relx=0.015, rely=0.42, relwidth=0.97, relheight=0.22)
        self.edit_outros.place(relx=0.015, rely=0.70, relwidth=0.97, relheight=0.22)
        self.edit_data.place(relx=0.74, rely=0.18, relwidth=0.1)
        self.edit_telefone.place(relx=0.54, rely=0.18, relwidth=0.1)

        # ============================================== MOSTRANDO LABEL =====================================================
        self.lcadastro.place(relx=0.39, rely=0.025)
        self.label_inicial.place(relx=0.03, rely=0.12)
        self.lidade.place(relx=0.375, rely=0.12)
        self.ldata_inicio.place(relx=0.74, rely=0.12)
        self.ltelefone.place(relx=0.54, rely=0.12)
        self.lhipotese.place(relx=0.44, rely=0.25)
        self.lprimeiro.place(x=19, y=165)
        self.loutros.place(x=19, y=295)


    def lista_frame(self):
        self.lista = ttk.Treeview(self.frame_dados, height = 3, column=('col1','col2','col3', 'col4'))    
        self.lista.heading('#0', text='')
        self.lista.heading('#1', text='NOME')
        self.lista.heading('#2', text='IDADE')
        self.lista.heading('#3', text='TELEFONE')
        self.lista.heading('#4', text='DATA DE INÍCIO')


        self.lista.column('#0', width =1)
        self.lista.column('#1', width =70)
        self.lista.column('#2', width =4)
        self.lista.column('#3', width =13)
        self.lista.column('#4', width =9)

        self.lista.place(relx=0.02, rely=0.1, relwidth=0.97, relheight=0.7)
        self.barra_rolagem = Scrollbar(self.frame_dados, orient='vertical')
        self.lista.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.98, rely=0.1, relwidth=0.01, relheight=0.7)


Janelas()
