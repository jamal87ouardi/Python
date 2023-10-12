from tkinter import *

window = Tk()

window.geometry("400x400")

window.title("Prix moto")

label1 = Label(window, text="Catégorie: ")
label1.pack(pady=10)

entryCat = Entry(window)
entryCat.pack(pady=10)

label2 = Label(window, text="Marque: ")
label2.pack(pady=10)

entryMarque = Entry(window)
entryMarque.pack(pady=10)




def choix_interne():
    exit

interne = IntVar()

check_interne = Checkbutton(window, text="client interne", variable=interne, command=choix_interne)

check_interne.pack(pady=10)

def calculer():
    
    total = 0

    cat = entryCat.get()
    marque = entryMarque.get()

    if(cat == "Sportif"):
        if(marque=="Suzuki"):
            total = 195000
        else :
            total = 180000
            
        if(interne.get() == 1 ):

            total = total*0.95
    else:
        if(cat == "trail"):
            if(marque=="Suzuki"):
                total = 250000
                if(interne.get() == 1 ):

                    total = total*0.95
            else :
                total = 200000

        else :
            if(marque=="Suzuki"):
                total = 150000
            else :
                total = 130000
            if(interne.get() == 1 ):

                total = total*0.95
    
    


    labelResultat.config(text=str(total)+ " MAD")





btnCalculer = Button(window, text="Calculer", command=calculer)

btnCalculer.pack(pady=10)

labelResultat = Label(window, text="--")

labelResultat.pack(pady=10)













window.mainloop()



