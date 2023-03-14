
import tkinter
from tkinter import *
from tkinter import ttk


#############CORES############
cor0 = "#444466" #black
cor1 = "#feffff" #white
cor2 = "#6f9fbd" #blue

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb864"
fundo = fundo_dia

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

janela.mainloop()