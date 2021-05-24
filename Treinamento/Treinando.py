from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
#root.title = ('Tela Inicial')
root.geometry("1350x700+5+5") 


class compon_consul(): ############# Botão  Novo ##################
    def widget_co(self , tip):
        self.bbotao = Button(tip, text = 'ok', command= self.nova_janela)
        self.bbotao = Button(tip, text = 'DELETAR', command= self.nova_janela)
        self.bbotao2 = Button(tip, text = 'VISUALIZAR', command= self.janela_visualizar)
        self.bbotao3 = Button(tip, text = 'VOLTAR', command= self.tope1.destroy)
        self.bbotao2.place(relx=0.50, rely=0.850)
        self.bbotao3.place(relx=0.60, rely=0.850)
        self.bbotao.place(relx=0.40, rely=0.850)
        
        #self.bbotao.place(x=350 , y=650)


    def menus(self):
        self.barraDeMenus = Menu(self.root )
        self.menuContatos = Menu(self.barraDeMenus, tearoff=0)
        self.menuContatos.add_command(label='NOVO', command=self.janela_inserir)
        self.menuContatos.add_command(label='PESQUISAR', command=self.janela_consultar)
        #self.menuContatos.add_command(label='DELETAR', command=self.semComando)
        self.menuContatos.add_separator()
        self.menuContatos.add_command(label='FECHAR', command=self.root.destroy)
        self.barraDeMenus.add_cascade(label='Contatos', menu=self.menuContatos)
        self.root.config(menu=self.barraDeMenus)
        

    def divisao_tela_co(self, tip1):
        print(tip1)
        self.frame_um = Frame(tip1)
        self.frame_um.place(relx=0.009, rely=0.01, relwidth=0.985, relheight=0.3)
        self.frame_um.configure(background='black')
        self.frame_um.configure(background='brown')
        self.frame_dois = Frame(tip1)
        self.frame_dois.place(relx=0.009, rely=0.32, relwidth=0.985, relheight=0.58)
        self.frame_dois.configure(background='brown')
        


    def lista_box_co(self):
        self.lista = ttk.Treeview(self.frame_um, height = 0, column=('col1','col2','col3', 'col4', 'col5', 'col6', 'col7'))    
        self.lista.heading('#0', text='')
        self.lista.heading('#1', text='NOME')
        self.lista.heading('#2', text='IDADE')
        self.lista.heading('#3', text='TELEFONE')
        self.lista.heading('#4', text='DATA DE INÍCIO')
        self.lista.heading('#5', text='HIPOTESE')
        self.lista.heading('#6', text='PRIMEIRO ATENDIMENTO')
        self.lista.heading('#7', text='OUTROS ATENDIMENTOs')

        self.lista.column('#0', width =2)
        self.lista.column('#1', width =100)
        self.lista.column('#2', width =4)
        self.lista.column('#3', width =13)
        self.lista.column('#4', width =9)
        self.lista.column('#5', width =100)
        self.lista.column('#6', width =100)
        self.lista.column('#7', width =100)

        self.lista.place(relx=0.02, rely=0.1, relwidth=0.97, relheight=0.7)
        self.barra_rolagem = Scrollbar(self.lista, orient='vertical')
        self.lista.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.98, rely=0.1, relwidth=0.01, relheight=0.7)
        self.lista.bind('<Double-1>', self.dois_clicks)


    def conecta_banco(self):
        self.banco = sqlite3.connect('Banco_Clientes.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS clientes (NOME text CHAR(50) NOT NULL, IDADE integer, DATA date, TELEFONE text, HIPOTESE text, PRIMEIRO text, OUTROS text)")
        
        self.banco.commit()


    def select_lista(self):
        
        self.lista.delete(*self.lista.get_children())
        lista1 = self.cursor.execute("""SELECT NOME, IDADE, DATA, TELEFONE, HIPOTESE, PRIMEIRO, OUTROS FROM clientes ORDER BY NOME ASC""")

        for i in lista1:
            self.lista.insert('',END, values=i)
            


    def preencher_co(self, trip):
        #=============== CRIANDO ENTRY ====================================
        self.edit_inicial_co = Entry(trip)
        self.edit_idade_co = Entry(trip)
        self.edit_hipotese_co = Entry(trip)
        self.edit_outros_co = Text(trip)
        self.edit_primeiro_co = Text(trip)
        self.edit_telefone_co = Entry(trip)
        self.edit_data_co = Entry(trip)

       #=============== CRIANDO LABEL ====================================

        self.lcadastro = Label(trip,bg="#808000",font=('white',16,'bold'), text='CADASTRO DE CLIENTES')
        self.label_inicial = Label( trip,font=('blak',11,'bold'),bg='brown', text='NOME')
        self.lidade = Label(trip,font=('blak',11,'bold'),bg='brown', text='IDADE')
        self.ldata_inicio = Label(trip,font=('blak',11,'bold'),bg='brown', text='DATA DE INICIO' )
        self.ltelefone = Label(trip,font=('blak',11,'bold'),bg='brown', text='TELEFONE')
        self.lhipotese = Label(trip,font=('blak',11,'bold'),bg='brown', text='HIPÓTESE DIAGNÓSTICA')
        self.lprimeiro = Label(trip,font=('blak',11,'bold'),bg='brown', text='PRIMEIRO ATENDIMENTO')
        self.loutros = Label(trip,font=('blak',11,'bold'),bg='brown', text='OUTROS ATENDIMENTOS')


    def inser_co(self):
        self.inicial1 = self.edit_inicial_co.get()
        self.primeiro1 = self.edit_primeiro_co.get("1.0", 'end')
        self.idade1 = self.edit_idade_co.get()
        self.dataInicio = self.edit_data_co.get()
        self.telefone1 = self.edit_telefone_co.get()
        self.hipotese1 = self.edit_hipotese_co.get()
        self.outros1 = self.edit_outros_co.get("1.0", 'end')

        self.cursor.execute('INSERT INTO clientes(NOME,IDADE,DATA,TELEFONE, HIPOTESE,PRIMEIRO,OUTROS)VALUES(?,?,?,?,?,?,?)',
        (self.inicial1, self.idade1, self.dataInicio, self.telefone1, self.hipotese1, self.primeiro1, self.outros1))

        self.banco.commit()
        self.limpar_co()
        #self.select_lista()
        


    def mostrar_co(self):
        # =============== MOSTRANDO CAIXA DE TEXTO E BOTÃO ================

        self.edit_inicial_co.place(relx=0.03, rely=0.18, relwidth=0.3)
        self.edit_idade_co.place(relx=0.375, rely=0.18, relwidth=0.1)
        self.edit_hipotese_co.place(relx=0.15, rely=0.3, relwidth=0.70)
        self.edit_primeiro_co.place(relx=0.015, rely=0.42, relwidth=0.97, relheight=0.45)
        #self.edit_outros_co.place(relx=0.015, rely=0.70, relwidth=0.97, relheight=0.22)
        self.edit_telefone_co.place(relx=0.675, rely=0.18, relwidth=0.1)
        self.edit_data_co.place(relx=0.875, rely=0.18, relwidth=0.1)


        # ====================== MOSTRANDO LABEL =====================================================
        self.lcadastro.place(relx=0.39, rely=0.025)
        self.label_inicial.place(relx=0.03, rely=0.12)
        self.lidade.place(relx=0.375, rely=0.12)
        self.ldata_inicio.place(relx=0.875, rely=0.13)
        self.lhipotese.place(relx=0.44, rely=0.25)
        self.ltelefone.place(relx=0.675, rely=0.13)
        self.lprimeiro.place(relx=0.03, rely=0.38)
        #self.loutros.place(x=19, y=295)
      

    def limpar_co(self):
        self.edit_inicial_co.delete(0, END)
        self.edit_idade_co.delete(0, END)
        self.edit_telefone_co.delete(0, END)
        self.edit_data_co.delete(0, END)
        self.edit_hipotese_co.delete(0, END)
        self.edit_outros_co.delete(1.0, END)
        self.edit_primeiro_co.delete(1.0, END)


    def dois_clicks(self,event):
        self.limpar_co()
        self.lista.selection()
        for n in self.lista.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.lista.item(n, 'values')
            self.edit_inicial_co.insert(END, col1)
            
            self.edit_idade_co.insert(END, col2)
            self.edit_telefone_co.insert(END, col3)
            self.edit_data_co.insert(END, col4)               
            self.edit_hipotese_co.insert(END, col5)
            self.edit_primeiro_co.insert(END, col6)
            self.edit_outros_co.insert(END, col7)


        


        


'''class compon(): #################### Botão Pesquizar ###############
    def widget(self , tip):
        self.bbotao = Button(tip, text = 'ok', command= self.nova_janela)
        self.bbotao = Button(tip, text = 'DELETAR', command= self.nova_janela)
        self.bbotao2 = Button(tip, text = 'VISUALIZAR', command= self.janela_visualizar)
        self.bbotao3 = Button(tip, text = 'VOLTAR', command= self.nova_janela)
        self.bbotao2.place(x=500 , y=650)
        self.bbotao3.place(x=600 , y=650)
        self.bbotao.place(x=700 , y=650)
        #self.bbotao.place(x=350 , y=650)


    def menus(self):
        self.barraDeMenus = Menu(self.root )
        self.menuContatos = Menu(self.barraDeMenus, tearoff=0)
        self.menuContatos.add_command(label='NOVO', command=self.janela_inserir)
        self.menuContatos.add_command(label='PESQUISAR', command=self.janela_consultar)
        self.menuContatos.add_command(label='DELETAR', command=self.semComando)
        self.menuContatos.add_separator()
        self.menuContatos.add_command(label='FECHAR', command=self.semComando)
        self.barraDeMenus.add_cascade(label='Contatos', menu=self.menuContatos)
        self.root.config(menu=self.barraDeMenus)


    def divisao_tela(self, tip1):
        print(tip1)
        self.frame_um = Frame(tip1)
        self.frame_um.place(relx=0.009, rely=0.01, relwidth=0.985, relheight=0.3)
        self.frame_um.configure(background='black')
        self.frame_um.configure(background='brown')
        self.frame_dois = Frame(tip1)
        self.frame_dois.place(relx=0.009, rely=0.32, relwidth=0.985, relheight=0.58)
        self.frame_dois.configure(background='brown')


    def lista_box(self):
        self.lista = ttk.Treeview(self.frame_um, height = 0, column=('col1','col2','col3', 'col4'))    
        self.lista.heading('#0', text='')
        self.lista.heading('#1', text='NOME')
        #self.lista.heading('#2', text='IDADE')
        #self.lista.heading('#3', text='TELEFONE')
        #self.lista.heading('#4', text='DATA DE INÍCIO')


        self.lista.column('#0', width =2)
        self.lista.column('#1', width =400)
        #self.lista.column('#2', width =4)
        #self.lista.column('#3', width =13)
        #self.lista.column('#4', width =9)
    

        self.lista.place(relx=0.02, rely=0.1, relwidth=0.97, relheight=0.7)
        self.barra_rolagem = Scrollbar(self.lista, orient='vertical')
        self.lista.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.98, rely=0.1, relwidth=0.01, relheight=0.7)
        #self.lista.bind('<Double-1>', self.dois_clicks)


    def preencher(self, trip):
        #=============== CRIANDO ENTRY ====================================
        self.edit_inicial = Entry(trip)
        self.edit_idade = Entry(trip)
        self.edit_telefone = Entry(trip)
        self.edit_data = Entry(trip)
        self.edit_hipotese = Entry(trip)
        self.edit_outros = Text(trip)
        self.edit_primeiro = Text(trip)

        #=============== CRIANDO LABEL ====================================

        self.lcadastro = Label(trip,bg="#808000",font=('white',16,'bold'), text='CADASTRO DE CLIENTES')
        self.label_inicial = Label( trip,font=('blak',11,'bold'),bg='brown', text='NOME')
        self.lidade = Label(trip,font=('blak',11,'bold'),bg='brown', text='IDADE')
        self.ldata_inicio = Label(trip,font=('blak',11,'bold'),bg='brown', text='DATA DE INICIO' )
        self.ltelefone = Label(trip,font=('blak',11,'bold'),bg='brown', text='TELEFONE')
        self.lhipotese = Label(trip,font=('blak',11,'bold'),bg='brown', text='HIPÓTESE DIAGNÓSTICA')
        self.lprimeiro = Label(trip,font=('blak',11,'bold'),bg='brown', text='PRIMEIRO ATENDIMENTO')
        self.loutros = Label(trip,font=('blak',11,'bold'),bg='brown', text='OUTROS ATENDIMENTOS')


    def mostrar(self):
        # =============== MOSTRANDO CAIXA DE TEXTO E BOTÃO ================

        self.edit_inicial.place(relx=0.30, rely=0.025, relwidth=0.5, relheight=0.08)
        self.edit_idade.place(relx=0.375, rely=0.18, relwidth=0.1)
        self.edit_hipotese.place(relx=0.15, rely=0.35, relwidth=0.70, relheight=0.22)
        self.edit_primeiro.place(relx=0.03, rely=0.65, relwidth=0.95, relheight=0.32)
        #self.edit_outros.place(relx=0.015, rely=0.70, relwidth=0.97, relheight=0.22)
        self.edit_data.place(relx=0.74, rely=0.18, relwidth=0.1)
        self.edit_telefone.place(relx=0.54, rely=0.18, relwidth=0.1)

        # ====================== MOSTRANDO LABEL =====================================================
        #self.lcadastro.place(relx=0.39, rely=0.025)
        self.label_inicial.place(relx=0.03, rely=0.12)
        self.lidade.place(relx=0.375, rely=0.12)
        self.ldata_inicio.place(relx=0.74, rely=0.12)
        self.ltelefone.place(relx=0.54, rely=0.12)
        self.lhipotese.place(relx=0.44, rely=0.25)
        self.lprimeiro.place(relx=0.03, rely=0.60)
        #self.loutros.place(x=19, y=295)'''


class compon_editar(): ############# Botão  Visualizar ##################
    def widget_ed(self , tip):
        self.bbotao = Button(tip, text = 'VOLTAR', command= self.tope1.destroy)
        self.bbotao2 = Button(tip, text = 'SALVAR', command= self.salve_ed) 
        self.bbotao.place(relx=0.50, rely=0.850)
        self.bbotao2.place(relx=0.60, rely=0.850)
        #self.bbotao.place_forget()


    def divisao_tela_ed(self, tip1):
        self.frame_dois = Frame(tip1)
        self.frame_dois.place(relx=0.009, rely=0.03, relwidth=0.985, relheight=0.95)
        self.frame_dois.configure(background='brown')


    def preencher_ed(self, trip):
        #=============== CRIANDO ENTRY ====================================
        self.edit_inicial = Entry(trip)
        self.edit_inicial.insert(END,self.edit_inicial_co.get())
        self.inicialED = self.edit_inicial.get()

        self.edit_outros = Text(trip)
        self.edit_outros.insert(END,self.edit_outros_co.get("1.0", 'end'))
        self.outroED = self.edit_outros.get("1.0", 'end')

        '''self.edit_primeiro = Text(trip)
        self.edit_telefone = Entry(trip)
        self.edit_data = Entry(trip)
        self.edit_idade = Entry(trip)
        self.edit_hipotese = Entry(trip)'''


       #=============== CRIANDO LABEL ====================================

        self.lcadastro = Label(trip,bg="#808000",font=('white',16,'bold'), text='CADASTRO DE CLIENTES')
        self.label_inicial = Label( trip,font=('blak',11,'bold'),bg='brown', text='NOME')
        self.lidade = Label(trip,font=('blak',11,'bold'),bg='brown', text='IDADE')
        self.lprimeiro = Label(trip,font=('blak',11,'bold'),bg='brown', text='PRIMEIRO ATENDIMENTO')
        self.loutros = Label(trip,font=('blak',11,'bold'),bg='brown', text='OUTROS ATENDIMENTOS')
        '''self.ldata_inicio = Label(trip,font=('blak',11,'bold'),bg='brown', text='DATA DE INICIO' )
        self.ltelefone = Label(trip,font=('blak',11,'bold'),bg='brown', text='TELEFONE')
        self.lhipotese = Label(trip,font=('blak',11,'bold'),bg='brown', text='HIPÓTESE DIAGNÓSTICA')'''


    def mostrar_ed(self):
        # =============== MOSTRANDO CAIXA DE TEXTO E BOTÃO ================
        
        self.edit_inicial.place(relx=0.03, rely=0.18, relwidth=0.3)
        #self.edit_idade.place(relx=0.375, rely=0.18, relwidth=0.1)
        #self.edit_hipotese.place(relx=0.15, rely=0.3, relwidth=0.70)
        #self.edit_primeiro.place(relx=0.015, rely=0.42, relwidth=0.97, relheight=0.52)
        self.edit_outros.place(relx=0.015, rely=0.30, relwidth=0.97, relheight=0.52)
        #self.edit_telefone.place(relx=0.675, rely=0.18, relwidth=0.1)
        #self.edit_data.place(relx=0.875, rely=0.18, relwidth=0.1)
        


        # ====================== MOSTRANDO LABEL =====================================================
        self.lcadastro.place(relx=0.39, rely=0.025)
        self.label_inicial.place(relx=0.03, rely=0.12)
        #self.lidade.place(relx=0.375, rely=0.12)
        #self.ldata_inicio.place(relx=0.875, rely=0.13)
        #self.lhipotese.place(relx=0.44, rely=0.25)
        #self.ltelefone.place(relx=0.675, rely=0.13)
        #self.lprimeiro.place(relx=0.03, rely=0.38)
        self.loutros.place(relx=0.400, rely=0.25)


    def inser_ed(self):
        self.inicial1 = self.edit_inicial.get()
        self.primeiro1 = self.edit_primeiro.get("1.0", 'end')
        self.idade1 = self.edit_idade.get()
        self.dataInicio = self.edit_data.get()
        self.telefone1 = self.edit_telefone.get()
        self.hipotese1 = self.edit_hipotese.get()
        self.outros1 = self.edit_outros.get("1.0", 'end')

        self.cursor.execute('INSERT INTO clientes(NOME,IDADE,DATA,TELEFONE, HIPOTESE,PRIMEIRO,OUTROS)VALUES(?,?,?,?,?,?,?)',
        (self.inicial1, self.idade1, self.dataInicio, self.telefone1, self.hipotese1, self.primeiro1, self.outros1))

        self.banco.commit()
        self.select_lista()


    def salve_ed(self):

        self.inicialED = self.edit_inicial.get()
        self.outroED = self.edit_outros.get("1.0", 'end')

        self.cursor.execute("UPDATE clientes SET OUTROS='{0}'WHERE NOME='{1}'".format(self.outroED, self.inicialED))
        
        
        #self.cursor.execute('UPDATE clientes SET OUTROS=  {0} WHERE NOME= {1} VALUES(?,?)' .format(self.outroED, self.inicialED))
        print(self.outroED)
        self.banco.commit()

             


    '''(NOME,IDADE,DATA,TELEFONE, HIPOTESE,PRIMEIRO,OUTROS)VALUES(?,?,?,?,?,?,?)',
    (self.inicial1, self.idade1, self.dataInicio, self.telefone1, self.hipotese1, self.primeiro1, self.outros1))'''




class constr(compon_consul, compon_editar):
    def __init__(self):
       
        self.root=root
        self.w, self.h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (self.w, self.h))
        self.menus()
        self.conecta_banco()

        

        


        root.mainloop()


    def nova_janela(self):
        self.tope = Toplevel()
        self.tope.geometry("%dx%d+0+0" % (self.w, self.h))
        self.divisao_tela(self.tope)
        print(self.tope)
        self.widget(self.tope)
        
        self.preencher(self.frame_dois)
        self.mostrar()
        self.lista_box()

    def semComando(self):
        print('')

    
    def janela_consultar(self): 
        self.tope1 = Toplevel()
        self.tope1.geometry("%dx%d+0+0" % (self.w, self.h))
        self.divisao_tela_co(self.tope1)
        self.widget_co(self.tope1)
        
        self.preencher_co(self.frame_dois)
        self.mostrar_co()
        self.lista_box_co()
        self.select_lista()
    

    def janela_inserir(self):
        self.tope1 = Toplevel()
        self.tope1.geometry("%dx%d+0+0" % (self.w, self.h))
        self.divisao_tela_ed(self.tope1)
        self.widget_ed(self.tope1)
        
        self.preencher_co(self.frame_dois)
        self.mostrar_co()
        

    def janela_visualizar(self):
        self.tope1 = Toplevel()
        self.tope1.geometry("%dx%d+0+0" % (self.w, self.h))
        self.divisao_tela_ed(self.tope1)
        self.widget_ed(self.tope1)
        
        self.preencher_ed(self.frame_dois)
        self.mostrar_ed()
        




constr()



