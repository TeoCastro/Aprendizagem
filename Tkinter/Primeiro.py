
from kivy.app import App
from kivy.uix.widget import Widget

from  tkinter import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def impdados():
    print('Oi')
    final.set( edit_inicial.get())

tela_inicial = Tk()
tela_inicial.title('Janela Principal')
tela_inicial.geometry("600x500")


final = StringVar()
final.set('oi')


label_inicial = Label(tela_inicial, textvariable = final)


edit_inicial = Entry()
botao_inicial = Button(tela_inicial,text = "Imprimir", command = impdados)

botao_inicial.place (x=290, y=140)
edit_inicial.place (x=240,y=100)
label_inicial.place(x=290, y=70)



tela_inicial.mainloop()
