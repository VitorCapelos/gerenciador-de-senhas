from tkinter import *
import sqlite3
import random
import string

MASTER_PASSWORD = '123456'

global service
global username
global password

global ARMAZEM_PASSWORD

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

OptionList = [
    'Salvar uma nova senha',
    'Listar senhas salvas',
    'Recuperar uma senha',
    'Gerar senha aleatória',
    'Sair'
]

def random_password(size=12, chars=string.ascii_uppercase + string.digits):
    clearScreen()
    lb1 = Label(app, text='Senha aleatória gerada:', font=('Arial', 12))
    lb1.pack(side='top', ipady=3)
    lb2 = Label(app, text=''.join(random.choice(chars) for x in range(size)), font=('Arial', 13), fg='green')
    lb2.pack(side='top')
    bt1 = Button(app, text='Gerar outra senha', font=('Arial', 12), command= random_password)
    bt1.pack(side='top')

#============================== FUNÇÕES SQLITE

def get_password(service):
    service = ed4.get()
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')
    teste = list(cursor.fetchall())
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')
    if len(teste) == 0:
        lb1 = Label(app, text='Serviço não encontrado!', font=('Arial', 12), fg='red')
        lb1.pack(side='top', ipady=10)
        lb1.after(2500,lb1.destroy)

    else:
        for user in cursor.fetchall():
            clearScreen()
            lb1 = Label(app, text='Usuário:', font=('Arial', 12))
            lb1.pack(side='top')
            lbUser = Label(app, text=f'{user[0]}', font=('Arial', 12), fg='red')
            lbUser.pack(side='top')
            lb2 = Label(app, text='Senha:', font=('Arial', 12))
            lb2.pack(side='top')
            lbPass = Label(app, text=f'{user[1]}', font=('Arial', 12), fg='green')
            lbPass.pack(side='top')
        bt1 = Button(app, text='Recuperar outra senha?', font=('Arial', 12), command= lambda: variable.set(f'{OptionList[2]}'))
        bt1.pack(side='top')

def insert_password(service, username, password, *args):
    service = ed1.get()
    username = ed2.get()
    password = ed3.get()
    if service != '' and username != '' and password != '':
        lb1 = Label(app, text='Serviço adicionado com sucesso!', font=('Arial', 12), fg='green')
        lb1.pack(side='top', ipady=10)
        lb1.after(2500,lb1.destroy)
        cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
        ''')
        conn.commit()
    else:
        lb1 = Label(app, text='Serviço não adicionado, faltam informações!', font=('Arial', 12), fg='red')
        lb1.pack(side='top', ipady=10)
        lb1.after(2500,lb1.destroy)

def show_services():
    lb0 = Label(app,text='Serviços adicionados:', font=('Arial', 12))
    lb0.pack(side='top')
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        lb1 = Label(app, text=f'{service}', font=('Arial', 12), fg='green')
        lb1.pack(side='top')

#============================== FIM DAS FUNÇÕES SQLITE

#============================== CÓDIGO DA GUI EM TKINTER

def validatorPassword(*args):
    ARMAZEM_PASSWORD = TEST_PASSWORD.get()
    
    if ARMAZEM_PASSWORD == MASTER_PASSWORD:
        clearScreen()
        
    else:
        exit()
        app.mainloop()

app = Tk()
app.geometry('350x300+200+200')
app.title('Gerenciador de Senhas')

def clearScreen():
    list = app.pack_slaves()
    for l in list:
        l.destroy()
    selectMenu()
    lb4 = Label(app, text='by: VitorCapelos', font=('Times New Roman', 10))
    lb4.pack( side='bottom', fill=BOTH)

lbLogin = Label(app, text='Insira a senha MASTER',font=('Arial', 12))
lbLogin.pack(side='top', ipady=3)
TEST_PASSWORD = Entry(app, show='*', font=('Arial', 12) , width=20)
TEST_PASSWORD.pack(side='top')
app.bind('<Return>', validatorPassword)
bt = Button(app, text='Fazer Login', font=('Arial', 12), width=12, command=validatorPassword)
bt.pack(side='top')
lb4 = Label(app, text='by: VitorCapelos', font=('Times New Roman', 10))
lb4.pack( side='bottom', fill=BOTH)

def selectMenu():
    global variable
    variable = StringVar(app)
    variable.set('Selecione uma opção:')
    menu = OptionMenu(app, variable, *OptionList)
    menu.config(width=90, font=('Arial', 12))
    menu.pack(side='top')
    optionMenu()

def optionMenu(*args):
    selectVariable = variable.get()

    if selectVariable == OptionList[0]:
        clearScreen()
        global ed1
        global ed2
        global ed3
        global ed4
        print(f'Você escolheu a opção {OptionList[0]}') 
        lb1 = Label(app, text='Qual o nome do serviço:', font=('Arial', 12))
        lb1.pack(side='top')
        ed1 = Entry(app)
        ed1.pack(side='top')
        lb2 = Label(app, text='Qual o nome de usuário:', font=('Arial', 12))
        lb2.pack(side='top')
        ed2 = Entry(app)
        ed2.pack(side='top')
        lb3 = Label(app, text='Qual a senha do serviço:', font=('Arial', 12))
        lb3.pack(side='top')
        ed3 = Entry(app)
        ed3.pack(side='top')
        service = ed1.get()
        username = ed2.get()
        password = ed3.get()
        app.bind('<Return>', lambda eff:insert_password(service, username, password))
        bt1 = Button(app, text='Inserir serviço', font=('Arial', 12) , command= lambda: insert_password(service, username, password))
        bt1.pack(side='top')


    if selectVariable == OptionList[1]:
        clearScreen()
        show_services()
        print(f'Você escolheu a opção: {OptionList[1]}')
    
    if selectVariable == OptionList[2]:
        clearScreen()
        print(f'Você escolheu a opção: {OptionList[2]}') 
        lb1 = Label(app,text='De qual serviço você gostaria \nde recuperar a senha?', width=40, font=('Arial', 12))
        lb1.pack(side='top')
        ed4 = Entry(app, width=40)
        ed4.pack(side='top')
        service = ed4.get()
        app.bind('<Return>', get_password)
        bt1 = Button(app, text='Buscar serviço', font=('Arial', 12), command= lambda: get_password(service))
        bt1.pack(side='top')

    if selectVariable == OptionList[3]:
        clearScreen()
        print(f'Você escolheu a opção: {OptionList[3]}') 
        random_password()
    
    if selectVariable == OptionList[4]:
        print(f'Você escolheu a opção: {OptionList[4]}')
        app.quit()

    variable.trace('w',optionMenu)

#============================== FIM DO CÓDIGO EM TKINTER

app.mainloop()
