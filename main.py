from requests import get
from tkinter import *
from json import loads

class Start():
        def __init__(self):
                self.window = Tk()
                self.window.geometry("500x400")
                self.window.title('Consulta CEP')
                self.window['bg'] = "light gray"
                self.Widgets()
                self.Show()
                self.window.mainloop()

        def Widgets(self):
                self.lb_text = Label(self.window, text="Consultar CEP" ,bg='light gray')
                self.lb_cep = Label(self.window, text="Digite seu CEP", bg='light gray')
                self.edt_cep = Entry(self.window)
                self.btn_con = Button(self.window, text="Consultar",command=self.ConsultaCep)
                self.list_lista = Listbox(self.window, width=40, height=15)
                self.lb_erro = Label(self.window, text="", bg='light gray',fg="red")

                               
        def ConsultaCep(self):                          
                if len(self.edt_cep.get()) == 8:
                        try:
                                self.resultado = loads(get('https://viacep.com.br/ws/'+self.edt_cep.get()+'/json/').text)
                                self.InserirDados()
                        except:
                                self.CepInvalido()
                else:
                        self.CepInvalido()

        def InserirDados(self):
                lista = ['logradouro','complemento','bairro','localidade','uf','ibge','gia','ddd','siafi']
                self.list_lista.delete(0,END)
                for l in lista:
                        if len(self.resultado[l]) >= 1:
                                self.list_lista.insert(END,l+": "+self.resultado[l])

        def CepInvalido(self):
                self.lb_erro['text'] = "CEP Invalido"

        def Show(self):
                self.lb_text.pack(pady=10)
                self.lb_cep.pack(pady=10)
                self.edt_cep.pack()
                self.btn_con.pack(pady=5)
                self.list_lista.pack()
                self.lb_erro.pack()

if __name__=="__main__":
        Start()
