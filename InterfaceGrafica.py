from Tkinter import *

#Cria janela
window = Tk()

#seta o titulo da janela
window.title('My programm')

#Entrada de texto
entry_text = Entry(window, width=80, )

#Gerenciador de geometria
entry_text.pack()

#Focar
entry_text.focus_set()

window.geometry('300x200')

def click_button():
    print(entry_text.get())
    print('Show!!!')

#Crriar butao
btn = Button(window, text = 'Clique Aqui', width=20, command=click_button )
btn.pack()

#Mantem a janela aberta
window.mainloop()