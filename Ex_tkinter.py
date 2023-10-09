from tkinter import *
# Tkinter Window
tkWindow = Tk();
tkWindow.geometry("400x400")

text1 = Label(tkWindow, text="Hello World!")
text1.pack(pady=10)

entry1 = Entry(tkWindow)
entry1.pack(pady=10)

entry2 = Entry(tkWindow)
entry2.pack(pady=10)


# Function to Change the Text
def change_text():
  a=int(entry1.get())
  b=int(entry2.get())
  c=a+b
  text1.config(text= c)

button1=Button(tkWindow, text='Change Text!',command=change_text)
button1.pack(pady=10)




tkWindow.mainloop()