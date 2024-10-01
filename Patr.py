# Importando dependencias
from tkinter import*
from tkinter import Tk, ttk
from tkinter.ttk import *
from tkinter import*
from PIL import Image, ImageTk

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  
co11 = "#f2f4f2"

# -------------------------- Criando a janela ---------------------------

janela = Tk ()
janela.title ("")
janela.geometry('380x500')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# -------------------------- Frames ---------------------------

frameCima = Frame(janela, width=380, height=50,  relief="flat",)
frameCima.grid(row=0, column=0,columnspan=2)

frameBaixo = Frame(janela,width=380, height=400, relief="flat")
frameBaixo.grid(row=2, column=0, pady=10)

frameResultado = Frame(janela,width=364, height=50, relief="flat")
frameResultado.grid(row=1, column=0, pady=10)

# Dividindo o Frame

frameAtivos = Frame(frameBaixo,width=180, height=370, relief="flat")
frameAtivos.grid(row=0, column=0, pady=0, padx=5)

framePassivos = Frame(frameBaixo,width=180, height=370, relief="flat")
framePassivos.grid(row=0, column=1, pady=0,)

app_ = Label(frameCima,text="Patrimônio Líquido",compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Arial 15'), fg=co4 )
app_.place(x=50, y=0)

# --------------------------- Entrando os Ativos ----------------------------

l_nome = Label(frameAtivos, text="Insira Ativos",padx=10, width=35, height=1,anchor=NW, font=('Verdana 11 '), fg=co0)
l_nome.place(x=0, y=0)

# Valor da casa
l_casa = Label(frameAtivos, text="Valor da casa", height=1,anchor=E, font=('Verdana 9 '), fg=co0)
l_casa.place(x=10, y=40)

e_valor_casa = Entry(frameAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_casa.place(x=10, y=65)

# Investimentos e Poupança
l_investimentos = Label(frameAtivos, text="Investimentos", height=1,anchor=E, font=('Verdana 9 '), fg=co0)

l_investimentos.place(x=10, y=230)
e_valor_investimentos = Entry(frameAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_investimentos.place(x=10, y=255)


# Veículos
l_veiculos = Label(frameAtivos, text="Veículos", height=1,anchor=E, font=('Verdana 9 '), fg=co0)
l_veiculos.place(x=10, y=165)

e_valor_veiculos = Entry(frameAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_veiculos.place(x=10, y=195)

#  Imóveis
l_imoveis = Label(frameAtivos, text="Imóveis", height=1,anchor=E, font=('Verdana 9 '), fg=co0)
l_imoveis.place(x=10, y=105)

e_valor_imovel = Entry(frameAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_imovel.place(x=10, y=125)


# Outros ativos
l_ativos = Label(frameAtivos, text="Outros ativos", height=1,anchor=E, font=('Verdana 9 '), fg=co0)
l_ativos.place(x=10, y=295)

e_outros_ativos = Entry(frameAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_outros_ativos.place(x=10, y=315)

janela.mainloop ()