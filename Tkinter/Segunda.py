from tkinter import *
import pandas as pd
import sqlite3


def semComandoPri():
    print('')

def nova_janela():
    top = Toplevel()


def menu():
    barraDeMenusPrincipal = Menu(tela_principal )
    menuContatosPrincipal = Menu(barraDeMenusPrincipal, tearoff=0 )
    menuContatosPrincipal.add_command(label='NOVO', command=nova_janela )
    menuContatosPrincipal.add_command(label='PESQUISAR', command=semComandoPri )
    menuContatosPrincipal.add_command(label='DELETAR', command=semComandoPri )
    menuContatosPrincipal.add_separator()
    menuContatosPrincipal.add_command(label='FECHAR', command=tela_principal.quit)
    barraDeMenusPrincipal.add_cascade(label='Contatos', menu=menuContatosPrincipal )
    tela_principal.config(menu=barraDeMenusPrincipal )


def planilhas():
    # ============= CARREGANDO PLANILHA DE CLIENTES DO EXCEL ============

    clientes = pd.read_excel('C:/Users/siuit/Documents/Python/Aprendizagem/Clientes do consultório.xlsx')

    nome = clientes['NOME'].fillna(' ')
    idade_clientes = clientes['IDADE'].fillna(' ')
    sexo = clientes['SEXO'].fillna(' ')
    telefone = clientes['TELEFONE'].fillna(' ')
    bairro = clientes['BAIRRO'].fillna(' ')
    queixainicial = clientes['QUEIXA INICIAL'].fillna(' ')


tela_principal = Tk()
tela_principal.title('Clientes')
tela_principal.geometry( "1150x700" )

menu()





tela_principal.mainloop()
