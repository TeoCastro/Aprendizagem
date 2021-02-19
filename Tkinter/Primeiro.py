from  tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3


def impdados():
    print('Oi')
    final.set( edit_inicial.get())

def insdados():
    inicial1 = edit_inicial.get()
    primeiro1 = edit_primeiro.get()
    idade1 = edit_idade.get()
    dataInicio = edit_data.get()
    telefone1 = edit_telefone.get()
    hipotese1 = edit_hipotese.get()
    outros1 = edit_outros.get()

    cursor.execute('INSERT INTO clientes(NOME,IDADE,DATA,TELEFONE, HIPOTESE,PRIMEIRO,OUTROS)VALUES(?,?,?,?,?,?,?)',(inicial1,idade1,dataInicio,telefone1, hipotese1,primeiro1,outros1))





#=================== CRIANDO E APRESENTANDO A JANELA PRINCIPAL ==================

tela_inicial = Tk()
tela_inicial.title('Janela Principal')
tela_inicial.geometry("1150x700")


#==================== CARREGANDO PLANILHA DE CLIENTES DO EXCEL ===================

#clientes = pd.read_excel('C:/Users/siuit/Documents/Python/Aprendizagem/Clientes do consultório.xlsx')

#nome = clientes['NOME'].fillna(' ')
#idade_clientes = clientes['IDADE'].fillna(' ')
#sexo = clientes['SEXO'].fillna(' ')
#telefone = clientes['TELEFONE'].fillna(' ')
#bairro = clientes['BAIRRO'].fillna(' ')
#queixainicial = clientes['QUEIXA INICIAL'].fillna(' ')



#==================== CRIANDO BANCO DE DADOS E TABELA ============================

banco = sqlite3.connect('Banco_Clientes.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (NOME text, IDADE integer, DATA date, TELEFONE text, HIPOTESE text, PRIMEIRO text, OUTROS text)")

#==================== CRIANDO VARIACEL ===========================================

final = StringVar()
final.set('NOME')

#===================== CRIANDO LABEL ========================================

lcadastro = Label(tela_inicial, text='CADASTRO DE CLIENTES')
label_inicial = Label(tela_inicial, textvariable=final)
lidade = Label(tela_inicial,text='IDADE')
ldata_inicio = Label(tela_inicial, text='DATA DE INICIO')
ltelefone = Label(tela_inicial, text='TELEFONE')
lhipotese = Label(tela_inicial, text='HIPÓTESE DIAGNÓSTICA')
lprimeiro= Label(tela_inicial, text='PRIMEIRO ATENDIMENTO')
loutros= Label(tela_inicial, text='OUTROS ATENDIMENTOS')

#===================== CRIANDO CAIXA DE TEXTO ===============================


edit_inicial = Entry()
edit_idade=Entry()
edit_telefone = Entry()
edit_data = Entry()
edit_hipotese=Entry()
edit_outros = Text()
edit_primeiro=Text()


#===================== CRIANDO BOTÃO ========================================

botao_inicial = Button(tela_inicial,text="Imprimir", command=impdados)



#===================== MOSTRANDO LABEL ======================================



lcadastro.place(x=490, y=10)
label_inicial.place(x=19, y=60)
lidade.place(x=530, y=60)
ldata_inicio.place(x=930,y=60)
ltelefone.place(x=710, y=60)
lhipotese.place(x=490, y=160)
lprimeiro.place(x=19, y=250)
loutros.place(x=19, y=450)


#====================== MOSTRANDO CAIXA DE TEXTO E BOTÃO ==================


botao_inicial.place(x=510, y=630, width=100, height=40)
edit_inicial.place(x=20, y=80, width=400)
edit_idade.place(x=533, y=80, width=30)
edit_hipotese.place(x=100, y=180, width=930)
edit_primeiro.place(x=20, y=270, width=1100, height= 150)
edit_outros.place(x=20, y=470, width=1100, height=150)
edit_data.place(x=933, y=80)
edit_telefone.place(x=717, y=80)


#====================== MOSTRANDO JANELA PRINCIPAL =======================

tela_inicial.mainloop()
