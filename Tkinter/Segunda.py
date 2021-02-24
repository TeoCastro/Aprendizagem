from tkinter import *
import pandas as pd
import sqlite3


def semComandoPri():
    print('')




tela_principal = Tk()
tela_principal.title('Clientes')
tela_principal.geometry( "1150x700" )

barraDeMenusPrincipal = Menu(tela_principal )
menuContatosPrincipal = Menu(barraDeMenusPrincipal, tearoff=0 )
menuContatosPrincipal.add_command(label='NOVO', command=semComandoPri )
menuContatosPrincipal.add_command(label='PESQUISAR', command=semComandoPri )
menuContatosPrincipal.add_command(label='DELETAR', command=semComandoPri )
menuContatosPrincipal.add_separator()
menuContatosPrincipal.add_command(label='FECHAR', command=tela_principal.quit)

barraDeMenusPrincipal.add_cascade(label='Contatos', menu=menuContatosPrincipal )

tela_principal.config(menu=barraDeMenusPrincipal )


tela_principal.mainloop()
