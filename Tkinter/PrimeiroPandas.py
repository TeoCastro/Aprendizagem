import pandas as pd
import numpy
from tkinter import *

def prijanela():
    tela_inicial = Tk()
    tela_inicial.title('Janela 1')
# criando os Label

    texto = Label(tela_inicial, text=nome, width= 40, justify=LEFT, bg="red")
    texto1 = Label(tela_inicial, text=sexo, width= 15, justify=LEFT, bg="yellow")
    texto2 = Label(tela_inicial, text=bairro, width=20, justify=LEFT, bg="pink")
    texto3 = Label(tela_inicial, text=cpf, width=20, justify=LEFT, bg="blue")

# mostrando os Label
    texto.pack(side=LEFT, fill=BOTH, expand=1)
    texto1.pack(side=LEFT, fill=BOTH, expand=1)
    texto2.pack(side=LEFT, fill=BOTH, expand=1)
    texto3.pack(side=LEFT, fill=BOTH, expand=1)

    tela_inicial.mainloop()





clientes = pd.read_excel('C:/Users/siuit/Documents/Python/PLANILHA_CLIENTES.XLSX')
tabclientes = pd.DataFrame(clientes)

sexo = clientes['SEXO'].fillna(' ')
nome = clientes['NOME'].fillna(' ')
cpf = clientes['CPF'].fillna(' ')
bairro = clientes['BAIRRO'].fillna(' ')



prijanela()