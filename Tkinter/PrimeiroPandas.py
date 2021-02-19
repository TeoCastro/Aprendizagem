import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import sqlite3




def prijanela():
    tela_inicial = Tk()
    tela_inicial.title('Janela 1')
    lista = Listbox(tela_inicial)


def mostrar():
    texto.pack(side=LEFT, fill=BOTH, expand=1)
    texto1.pack(side=LEFT, fill=BOTH, expand=1)
    texto2.pack(side=LEFT, fill=BOTH, expand=1)
    texto3.pack(side=LEFT, fill=BOTH, expand=1)
    texto4.pack(side=LEFT, fill=BOTH, expand=1)
    texto5.pack(side=LEFT, fill=BOTH, expand=1)
    texto6.pack(side=LEFT, fill=BOTH, expand=1)
    lista.pack()


# prijanela()
    
# criando os Label

texto = Label(tela_inicial, text=nome, width= 40, justify=LEFT, bg="red")
texto1 = Label(tela_inicial, text=sexo, width= 15, justify=LEFT, bg="yellow")
texto2 = Label(tela_inicial, text=bairro, width=20, justify=LEFT, bg="pink")
texto3 = Label(tela_inicial, text=cpf, width=20, justify=LEFT, bg="blue")
texto4 = Label(tela_inicial, text=telefone, width=20, justify=LEFT, bg="gray")
texto5 = Label(tela_inicial, text=datanasc, width=20, justify=LEFT, bg="brown")
texto6 = Label(tela_inicial, text=queixainicial, width=20, justify=LEFT, bg="beige")
lista.insert(0, texto)
lista.insert(0, Label)


# mostrando os Label
mostrar()


tela_inicial.mainloop()





clientes = pd.read_excel('C:/Users/siuit/Documents/Python/PLANILHA_CLIENTES.XLSX')
#tabclientes = pd.DataFrame(clientes)
#print(tabclientes)
#tabclientes.head(30)
clientes.head(30)

sexo = clientes['SEXO'].fillna(' ')
nome = clientes['NOME'].fillna(' ')
cpf = clientes['CPF'].fillna(' ')
bairro = clientes['BAIRRO'].fillna(' ')
telefone = clientes['TELEFONE'].fillna(' ')
datanasc = clientes['DATA DE NASC'].fillna(' ')
queixainicial = clientes['QUEIXA INICIAL'].fillna(' ')
#plt.plot(clientes['TELEFONE'])
#plt.show()
#plt.pie(clientes['TELEFONE'])
#plt.show()

prijanela()