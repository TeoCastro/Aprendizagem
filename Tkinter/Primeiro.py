import sqlite3
from tkinter import *

''''==============================================================================================================
=============================================== FUNÇÕES ======================================================
=============================================================================================================='''



def nova_janela():
    # ============================== CRIANDO NOVA JANELA PARA MOSTRAR OS REGISTROS ================================

    top = Toplevel()
    top.title('Janela Busca')
    lb_registro = Listbox(top)
    lb_registro.place(x=10, y=10, width=600, height=450)
    top.geometry("800x500")
    cursor.execute('SELECT * FROM clientes')
    pesq = cursor.fetchall()
    print(pesq)
    print("Número total de registros retornados: ", cursor.rowcount)
    for linha in pesq:
        print("Nome:", linha[0])
        print("Idade:", linha[1])
        print("Início:", linha[2], "\n")
        # ==== carregando listbox com os nomes dos registros =====
        lb_registro.insert(END, linha[0])





def semComando():
    print('')


def salv_reg(inicial2,primeiro2,idade2,dataInicio2,hipotese2,outros2,telefone2):
    #print(inicial2)
    
    # =========================================== GRAVANDO O REGISTRO =============================================
 
    cursor.execute('INSERT INTO clientes(NOME,IDADE,DATA,TELEFONE, HIPOTESE,PRIMEIRO,OUTROS)VALUES(?,?,?,?,?,?,?)',
    (inicial2, idade2, dataInicio2, telefone2, hipotese2, primeiro2, outros2))

    banco.commit()

def janela_principal():
    # ============================================= CONSTRUINDO MENUS ====================================================

    barraDeMenus = Menu(tela_inicial )
    menuContatos = Menu(barraDeMenus, tearoff=0)
    menuContatos.add_command(label='NOVO', command=ins_janela)
    menuContatos.add_command(label='PESQUISAR', command=nova_janela)
    menuContatos.add_command(label='DELETAR', command=semComando)
    menuContatos.add_separator()
    menuContatos.add_command(label='FECHAR', command=tela_inicial.quit)
    barraDeMenus.add_cascade(label='Contatos', menu=menuContatos)
    tela_inicial.config(menu=barraDeMenus)
    tela_inicial.mainloop()


def ins_janela():
    # ============================== CRIANDO NOVA JANELA PARA MOSTRAR OS REGISTROS ================================

    topins = Toplevel()
    topins.title('Janela Inserir')
    topins.geometry("1150x700")


    edit_inicial = Entry(topins)
    edit_idade = Entry(topins)
    edit_telefone = Entry(topins)
    edit_data = Entry(topins)
    edit_hipotese = Entry(topins)
    edit_outros = Text(topins)
    edit_primeiro = Text(topins)



    inicial1 = edit_inicial.get()
    print (inicial1)
    primeiro1 = edit_primeiro.get("1.0", 'end')
    idade1 = edit_idade.get()
    dataInicio = edit_data.get()
    telefone1 = edit_telefone.get()
    hipotese1 = edit_hipotese.get()
    outros1 = edit_outros.get("1.0", 'end')

# inicial1,primeiro1,idade1,dataInicio,hipotese1,outros1,telefone1
 
    # =========================================== LIMPANDO OS CAMPOS ==============================================

    '''edit_inicial.delete(0, END)
    edit_primeiro.delete(1.0, END + '-1c')
    edit_idade.delete(0, END)
    edit_data.delete(0, END)
    edit_telefone.delete(0, END)
    edit_hipotese.delete(0, END)
    edit_outros.delete(1.0, END + '-1c')'''

    '''print('Geraldo')
    print(idade1)
    print(dataInicio)
    print(telefone1)
    print(hipotese1)
    print(primeiro1)
    print(outros1)'''

    # =========================================== CRIANDO CAIXA DE TEXTO =================================================
    # =============================================== CRIANDO BOTÃO ======================================================

    botao_inicial = Button(topins, text='Salvar', command=salv_reg(inicial1,primeiro1,idade1,dataInicio,hipotese1,outros1,telefone1))
    botao_mostrar = Button(topins, text='Mostrar', command=nova_janela)


    # ===================================== MOSTRANDO CAIXA DE TEXTO E BOTÃO =============================================

    botao_mostrar.place(x=610, y=630, width=100, height=40)
    botao_inicial.place(x=450, y=630, width=100, height=40)
    edit_inicial.place(x=20, y=80, width=400)
    edit_idade.place(x=533, y=80, width=30)
    edit_hipotese.place(x=100, y=180, width=930)
    edit_primeiro.place(x=20, y=270, width=1100, height=150)
    edit_outros.place(x=20, y=470, width=1100, height=150)
    edit_data.place(x=933, y=80)
    edit_telefone.place(x=717, y=80)
    # ============================================== CRIANDO LABEL ========================================================

    lcadastro = Label(topins, text='CADASTRO DE CLIENTES')
    label_inicial = Label( topins, textvariable=final)
    lidade = Label(topins, text='IDADE')
    ldata_inicio = Label(topins, text='DATA DE INICIO' )
    ltelefone = Label(topins, text='TELEFONE')
    lhipotese = Label(topins, text='HIPÓTESE DIAGNÓSTICA')
    lprimeiro = Label(topins, text='PRIMEIRO ATENDIMENTO')
    loutros = Label(topins, text='OUTROS ATENDIMENTOS')


    # ============================================== MOSTRANDO LABEL =====================================================
    lcadastro.place(x=490, y=10)
    label_inicial.place(x=19, y=60)
    lidade.place(x=530, y=60)
    ldata_inicio.place(x=930, y=60)
    ltelefone.place(x=710, y=60)
    lhipotese.place(x=490, y=16)
    lprimeiro.place(x=19, y=250)
    loutros.place(x=19, y=450)


    







# =====================================================================================================================
# ================================== CRIANDO E APRESENTANDO A JANELA PRINCIPAL =======================================
# =====================================================================================================================


tela_inicial = Tk()
tela_inicial.title('Janela Consulta')
tela_inicial.geometry("1250x700 + 600 + 600")
#tela_inicial.geometry("1150x700")
# ================================= INICIANDO AS VARIÁVEIS ANTES DE RODAR A FUNÇÃO ===================================



'''inicial1 = ''
primeiro1 = ''
idade1 = ''
dataInicio = ''
hipotese1 = ''
outros1 = ''
telefone1 = '' '''



# ===================================== CRIANDO BANCO DE DADOS E TABELA ===============================================

banco = sqlite3.connect('Banco_Clientes.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (NOME text, IDADE integer, DATA date, TELEFONE text, HIPOTESE text, PRIMEIRO text, OUTROS text)")

# =========================================== CRIANDO VARIAVEL ========================================================

final = StringVar()
final.set('NOME COMPLETO')




janela_principal()

