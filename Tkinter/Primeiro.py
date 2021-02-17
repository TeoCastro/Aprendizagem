from  tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3


def impdados():
    print('Oi')
    final.set( edit_inicial.get())


#=================== CRIANDO E APRESENTANDO A JANELA PRINCIPAL ==================

tela_inicial = Tk()
tela_inicial.title('Janela Principal')
tela_inicial.geometry("600x500")


#==================== CARREGANDO PLANILHA DE CLIENTES DO EXCEL ===================

clientes = pd.read_excel('C:/Users/siuit/Documents/Python/PLANILHA_CLIENTES.XLSX')


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
lhipotese = Label(tela_inicial, text='HIPÓTESE DIAGNÓSTICA')
lprimeiro= Label(tela_inicial, text='PRIMEIRO ATENDIMENTO')
loutros= Label(tela_inicial, text='OUTROS ATENDIMENTOS')

#===================== CRIANDO CAIXA DE TEXTO ===============================


edit_primeiro=Text()
edit_hipotese=Entry()
edit_idade=Entry()
edit_inicial = Entry()
edit_outros = Text()

#===================== CRIANDO BOTÃO ========================================

botao_inicial = Button(tela_inicial,text="Imprimir", command=impdados)



#===================== MOSTRANDO LABEL ======================================



lcadastro.place(x=240, y=20)
label_inicial.place(x=19, y=40)
lidade.place(x=19, y=100)
lhipotese.place(x=19, y=160)
lprimeiro.place(x=19, y=220)
loutros.place(x=19, y=360)


#====================== MOSTRANDO CAIXA DE TEXTO E BOTÃO ==================


botao_inicial.place(x=390, y=270)
edit_inicial.place(x=20, y=60, width=400)
edit_idade.place(x=20, y=120, width=30)
edit_hipotese.place(x=20, y=180, width=550)
edit_primeiro.place(x=20, y=240, width=300, height= 100)
edit_outros.place(x=20, y=380, width=300, height=100)


#====================== MOSTRANDO JANELA PRINCIPAL =======================

tela_inicial.mainloop()
