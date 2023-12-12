#importando o TKINTER--

from tkinter import *
from tkinter import ttk

cor1 = "#212121" #Preto
cor2 = "#e0e0e0" #Branco
cor3 = "#1c1c1c" #Preto display
cor4 = "#d6d6d6" #Cinza
cor5 = "#9e9e9b" #Cinza Operações

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x324')
janela.configure(bg=cor1)

#criando o frame do display da calculadora----------------

frame_tela = Frame(janela, width=235, height=60, bg= cor3)
frame_tela.grid(row=0, column= 0, pady=0)

#criando o frame do teclado da calculadora--------

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variavel todos valores 

todos_valores = ''

#Criando função

def inputar_valores(event):
    
    global todos_valores

    todos_valores = todos_valores + str(event)  

#passando o valor para a tela
    valor_texto.set(todos_valores)

#função para calcular

def calcular():
    global todos_valores
    global resultado
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#função limpar display

def limpar_display():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")





#criando label
valor_texto= StringVar()

app_label = Label(frame_tela, textvariable= valor_texto, width=16, height=2, padx=4, relief=FLAT, anchor="e", justify= RIGHT, font=('Ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0, y=10)

#Botões

#primeira fileira------------------------------------------------------------------------------------------------------------------------------------------------------

b_1 = Button(frame_corpo, command= limpar_display, text="C", width=11, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: inputar_valores('%'), text="%", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command= lambda: inputar_valores('/'), text="/", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

#segunda fileira----------------------------------------------------------------------------------------------------------------

b_4 = Button(frame_corpo, command= lambda: inputar_valores('7'), text="7", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52) 
b_5 = Button(frame_corpo, command= lambda: inputar_valores('8'), text="8", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command= lambda: inputar_valores('9'), text="9", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command= lambda: inputar_valores('*'), text="*", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

#terceira fileira---------------------------------------------------------------------------------------------------------------

b_8 = Button(frame_corpo, command= lambda: inputar_valores('4'), text="4", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command= lambda: inputar_valores('5'),text="5", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command= lambda: inputar_valores('6'), text="6", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command= lambda: inputar_valores('-'), text="-", width=5, height=2, bg=cor4, fg=cor1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

#quarta fileira-------------------------------------------------------------------------------------------------------------------

b_12 = Button(frame_corpo, command= lambda: inputar_valores('1'), text="1", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command= lambda: inputar_valores('2'), text="2", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command= lambda: inputar_valores('3'), text="3", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command= lambda: inputar_valores('+'), text="+", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

#quinta fileira------------------------------------------------------------------------------------------------------------------

b_16 = Button(frame_corpo, command= lambda: inputar_valores('0'), text="0", width=11, height=2, bg=cor3, fg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command= lambda: inputar_valores('.'), text=".", width=5, height=2, bg=cor3, fg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor4, fg=cor1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)



janela.mainloop()