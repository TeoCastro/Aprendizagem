import pandas as pd
import numpy
from tkinter import *

def prijanela():
    tela_inicial = Tk()
    tela_inicial.title('Janela 1')
    Label(tela_inicial, text=tabclientes3['SEXO'], justify=LEFT).pack()
    tela_inicial.mainloop()
    
clientes = pd.read_excel('C:/Users/siuit/Documents/Python/PLANILHA_CLIENTES.XLSX')

tabclientes = pd.DataFrame(clientes)

tabclientes3 = tabclientes.loc[tabclientes['SEXO']== 'F']
print (tabclientes3)

prijanela()

