from tkinter import *
from tkinter import ttk

root = Tk()
#root.title = ('Tela Inicial')
root.geometry("1350x700+5+5") 


class compon_consul(): ############# Botão  Novo ##################
    def widget_co(self , tip):
        self.bbotao = Button(tip, text = 'ok', command= self.nova_janela)
        self.bbotao = Button(tip, text = 'DELETAR', command= self.nova_janela)
        self.bbotao2 = Button(tip, text = 'VISUALIZAR', command= self.janela_visualizar)
        self.bbotao3 = Button(tip, text = 'VOLTAR', command= self.tope1.destroy)
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


    def preencher_co(self, trip):
        #=============== CRIANDO ENTRY ====================================
        self.edit_inicial = Entry(trip)
        self.edit_idade = Entry(trip)
        self.edit_hipotese = Entry(trip)
        self.edit_outros = Text(trip)
        self.edit_primeiro = Text(trip)
        self.edit_telefone = Entry(trip)
        self.edit_data = Entry(trip)

       #=============== CRIANDO LABEL ====================================

        self.lcadastro = Label(trip,bg="#808000",font=('white',16,'bold'), text='CADASTRO DE CLIENTES')
        self.label_inicial = Label( trip,font=('blak',11,'bold'),bg='brown', text='NOME')
        self.lidade = Label(trip,font=('blak',11,'bold'),bg='brown', text='IDADE')
        self.ldata_inicio = Label(trip,font=('blak',11,'bold'),bg='brown', text='DATA DE INICIO' )
        self.ltelefone = Label(trip,font=('blak',11,'bold'),bg='brown', text='TELEFONE')
        self.lhipotese = Label(trip,font=('blak',11,'bold'),bg='brown', text='HIPÓTESE DIAGNÓSTICA')
        self.lprimeiro = Label(trip,font=('blak',11,'bold'),bg='brown', text='PRIMEIRO ATENDIMENTO')
        self.loutros = Label(trip,font=('blak',11,'bold'),bg='brown', text='OUTROS ATENDIMENTOS')


    def mostrar_co(self):
        # =============== MOSTRANDO CAIXA DE TEXTO E BOTÃO ================

        self.edit_inicial.place(relx=0.03, rely=0.18, relwidth=0.3)
        self.edit_idade.place(relx=0.375, rely=0.18, relwidth=0.1)
        self.edit_hipotese.place(relx=0.15, rely=0.3, relwidth=0.70)
        self.edit_primeiro.place(relx=0.015, rely=0.42, relwidth=0.97, relheight=0.52)
        #self.edit_outros.place(relx=0.015, rely=0.70, relwidth=0.97, relheight=0.22)
        self.edit_telefone.place(relx=0.675, rely=0.18, relwidth=0.1)
        self.edit_data.place(relx=0.875, rely=0.18, relwidth=0.1)


        # ====================== MOSTRANDO LABEL =====================================================
        self.lcadastro.place(relx=0.39, rely=0.025)
        self.label_inicial.place(relx=0.03, rely=0.12)
        self.lidade.place(relx=0.375, rely=0.12)
        self.ldata_inicio.place(relx=0.875, rely=0.13)
        self.lhipotese.place(relx=0.44, rely=0.25)
        self.ltelefone.place(relx=0.675, rely=0.13)
        self.lprimeiro.place(relx=0.03, rely=0.38)
        #self.loutros.place(x=19, y=295)


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

        self.bbotao.place(x=650 , y=650)
        #self.bbotao.place_forget()



    def divisao_tela_ed(self, tip1):
        self.frame_dois = Frame(tip1)
        self.frame_dois.place(relx=0.009, rely=0.03, relwidth=0.985, relheight=0.95)
        self.frame_dois.configure(background='brown')


    def preencher_ed(self, trip):
        #=============== CRIANDO ENTRY ====================================
        self.edit_inicial = Entry(trip)
        #self.edit_idade = Entry(trip)
        #self.edit_hipotese = Entry(trip)
        self.edit_outros = Text(trip)
        #self.edit_primeiro = Text(trip)
        #self.edit_telefone = Entry(trip)
        #self.edit_data = Entry(trip)

       #=============== CRIANDO LABEL ====================================

        self.lcadastro = Label(trip,bg="#808000",font=('white',16,'bold'), text='CADASTRO DE CLIENTES')
        self.label_inicial = Label( trip,font=('blak',11,'bold'),bg='brown', text='NOME')
        self.lidade = Label(trip,font=('blak',11,'bold'),bg='brown', text='IDADE')
        #self.ldata_inicio = Label(trip,font=('blak',11,'bold'),bg='brown', text='DATA DE INICIO' )
        #self.ltelefone = Label(trip,font=('blak',11,'bold'),bg='brown', text='TELEFONE')
        #self.lhipotese = Label(trip,font=('blak',11,'bold'),bg='brown', text='HIPÓTESE DIAGNÓSTICA')
        self.lprimeiro = Label(trip,font=('blak',11,'bold'),bg='brown', text='PRIMEIRO ATENDIMENTO')
        self.loutros = Label(trip,font=('blak',11,'bold'),bg='brown', text='OUTROS ATENDIMENTOS')


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


class constr(compon_consul, compon_editar):
    def __init__(self):
       
        self.root=root
        self.menus()

        

        


        root.mainloop()


    def nova_janela(self):
        self.tope = Toplevel()
        self.tope.geometry("1350x700+5+5")
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
        self.tope1.geometry("1350x700+5+5")
        self.divisao_tela_co(self.tope1)
        self.widget_co(self.tope1)
        
        self.preencher_co(self.frame_dois)
        self.mostrar_co()
        self.lista_box_co()
    

    def janela_inserir(self):
        self.tope1 = Toplevel()
        self.tope1.geometry("1350x700+5+5")
        self.divisao_tela_ed(tope1)
        self.widget_co(tope1)
        
        self.preencher_co(self.frame_dois)
        self.mostrar_co()
        

    def janela_visualizar(self):
        self.tope1 = Toplevel()
        self.tope1.geometry("1350x700+5+5")
        self.divisao_tela_ed(self.tope1)
        self.widget_ed(self.tope1)
        
        self.preencher_ed(self.frame_dois)
        self.mostrar_ed()


    def fechar(self):
        Toplevel.destroy()
        



constr()



