
from tkinter import *

tkWindow = Tk();
tkWindow.geometry("600x600")
tkWindow.config(bg="#c9f5dd")

text1 = Label(tkWindow, text="valeur de A")
text1.pack(pady=10)

entry1 = Entry(tkWindow)
entry1.pack(pady=10)


text2 = Label(tkWindow, text="B")
text2.pack(pady=10)

entry2 = Entry(tkWindow)
entry2.pack(pady=10)


# Function to Change the Text
def somme():
  a=int(entry1.get())
  b=int(entry2.get())
  c=a+b
  text3.config(text= c)

button1=Button(tkWindow, text='somme',command=somme)
button1.pack(pady=10)

text3 = Label(tkWindow, text="--")
text3.pack(pady=10)

tkWindow.mainloop()