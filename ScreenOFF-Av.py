import PySimpleGUI as psg

#Usuarios e senhas
Usuarios = ['joao','sii','maria']
Senhas = ['1234','1212','4321']
Pessoas = ['JOAO VICTOR','SIMONE','MARIA']

#JANELAS DE USO

def janelaFundo():
    layout = [
        [psg.Text('1',size=2)]
    ]

    return psg.Window('Fundo',layout=layout,finalize=True,background_color='black',size=(1500,1000))


def janelaLogin():
    
    layout = [
        [psg.Text('Login',size=10), psg.Input(size=15,key='Login')],
        [psg.Text('Password',size=10), psg.Input(size=15,key='Password')],
        [psg.Button('Logar',size=10), psg.Button('Sair',size=10)]
    ]

    layoutCentro = [
        [psg.Column([[psg.Text('',size=(2,0))]]),
         psg.Column(layout),
         psg.Column([[psg.Text('',size=(2,0))]])]
    ]

    return psg.Window('Tela de login',layout=layoutCentro,finalize=True)

def janelaUso(Usuario):

    layout = [
        [psg.Text(Usuario,size= 30,key='user'), psg.Button('X',button_color='red')]
    ]

    return psg.Window('Tela de Uso',layout=layout,finalize=True)

#CRIAR JANELAS
janela3,janela1,janela2 = janelaFundo(), janelaLogin(), None


#LOOP PARA LEITURA DOS EVENTOS

while True:

    window, event, values = psg.read_all_windows()
    #Quando a janela for fechada
    if window == janela3 and event == psg.WIN_CLOSED:
        break
    if window == janela1 and event == psg.WIN_CLOSED:
        break
    elif window == janela1:
        if event == 'Logar':
            Login = values['Login']
            Senha = values['Password']
            num = None

            try:
                num = Usuarios.index(Login)
            except:
                psg.popup('Usuario/Senha errado')
                continue
            
            #Procurar usuario
            if Senhas[num] == Senha:
                print('acertou')
                janela2 = janelaUso(Pessoas[num])
                janela1.hide()
                janela3.hide()
            else:
                psg.popup('Senha/Usuario errado')


    elif window == janela2:
        if event == 'X' or event == psg.WIN_CLOSED:
            janela2.hide()
            janela3.un_hide()
            janela1.un_hide()