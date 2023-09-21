#Les entrée

Sv=int(input("Entrer le nombre de Sv: "))
Sk=int(input("Entrer le nombre de Sk: "))
So=int(input("Entrer le nombre de So: "))



#Traitement

if Sv>2:
    Psv = Sv*2000*0.75

else:
    Psv = Sv*2000

if Sk>2:
    Psk = Sk*2800*0.68
else:
    Psk = Sk*2800

Pso=So*380030.9

Pt=Psv+Psk+Pso


#Sortie

print(f"Le prix de la commande est {Pt}")