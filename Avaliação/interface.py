from tkinter import *
import tkinter as tk

def fun_dados():
    nome = E_nome.get()
    mensagem = E_men.get()
    
    wind2 = Tk()
    wind2.title("Para 2º Semestre - Univale")
    wind2.geometry("280x180")

    resultado = f'{nome} diz: {mensagem}.'

    saida = Label(wind2, text=resultado)
    saida.grid(column=0, row=0)

    wind2.mainloop()
    


wind = Tk()
wind.title("Entrada de mensagem")
wind.geometry("280x180")

txt_or = Label(wind, text="Você consegui fazer isso?? - 2º Semestre - UNIVALE", fg='red')
txt_or.grid(column=0, row=0)

L_nome = Label(wind, text="Nome:")
L_nome.grid(column=0, row=1, padx=10, pady=5, sticky=W)
E_nome = tk.Entry(wind, width=40)
E_nome.grid(column=0, row=2)

L_men = Label(wind, text="Mensagem:")
L_men.grid(column=0, row=3, padx=10, pady=5, sticky=W)
E_men = tk.Entry(wind, width=40)
E_men.grid(column=0, row=4)

botao = Button(wind,padx=10, pady=1, width=31, text='Enviar', command=fun_dados)
botao.grid(column=0, row=5,)
botao = Button(wind,padx=10, pady=1, width=31, text='Enviar', command=wind.destroy)
wind.mainloop()