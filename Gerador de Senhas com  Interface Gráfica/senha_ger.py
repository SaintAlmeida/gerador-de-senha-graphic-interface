import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
       
       #layout do Gerador
       
        sg.theme('Black')
        layout = [ 
            [sg.Text('Site/Software',size=(10,1)),
             sg.Input(key='site',size=(20,1))],
              [sg.Text('E-mail/Usuário',size=(10,1)),
             sg.Input(key='usuario',size=(20,1))],
             [sg.Text('Quantidade de Caracteres'),sg.Combo(values=list(range(30)),key='total chars',default_value=1,size=(3,1))],
             [sg.Output(size=(32,5))],
             [sg.Button('Gerar Senha')]
        ]

        #Janela do Gerador

        self.janela = sg.Window('Gerador de Senhas',layout)
                           



      

    def Iniciar(self):
        while True:
            evento,valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha,valores)
    
    
    def gerar_senha(self,valores):
     char_list = 'ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuvwyxz123456789!'
     chars = random.choices(char_list, k=int(valores['total chars']))
     new_pass = ''.join(chars)
     return new_pass
    
    def Salvar_Senha(self,nova_senha,valores):
        with open('senhas.txt','a', newline='') as arquivo:
            arquivo.write(f'site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}')
            print('Arquivo Salvo')
       

gen = PassGen()
gen.Iniciar()
