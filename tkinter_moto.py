from tkinter import *
from tkinter import ttk

selected_cat="cross"

selected_mar="Suzuki"

def on_cat_select(event):
    selected_cat = combobox_cat.get()
    
def on_marque_select(event):
    selected_mar = combobox_mar.get()
    
def on_click():
    print()

# Create a Tkinter window
window = Tk()
window.geometry("400x400")
window.title("Moto Example")

# Create a label
label = Label(window, text="Selectionner une catégorie:")
label.pack(pady=10)

# Create a Combobox widget
cats = ["Cross", "Trail", "Basic"]
combobox_cat = ttk.Combobox(window, values=cats)
combobox_cat.pack()

combobox_cat.set(cats[0])

# Bind the event handler to the selection
combobox_cat.bind("<<ComboboxSelected>>", on_cat_select)



label = Label(window, text="Selectionner une marque:")
label.pack(pady=10)

# Create a Combobox widget
marques = ["Suzuki", "Yamaha"]
combobox_mar = ttk.Combobox(window, values=marques)
combobox_mar.pack()

combobox_mar.set(marques[0])

# Bind the event handler to the selection
combobox_mar.bind("<<ComboboxSelected>>", on_marque_select)


btnCal = Button(window, text="Calculer",command=on_click)
btnCal.pack(pady=10)

# Create a label to display the selected item
result_label = Label(window, text="")
result_label.pack()

window.mainloop()
