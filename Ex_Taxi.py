# Les entrées

hd=int(input("Entrer heure départ: "))
np=int(input("Entrer le nombre de passagers: "))
d=float(input("Entrer la distance: "))


# Traitement

if 6<hd<20:
    if np==1:
        p=20
    else:
        if np==2 or np==3:
            p=50
        else:
            if np==4 or np==5:
                p=75
            else:
                print("Erreur")
else:
    if np==1:
        p=20*1.2
    else:
        if np==2 or np==3:
            p=50*1.2
        else:
            if np==4 or np==5:
                p=75*1.2
            else:
                print("Erreur")

if d>=6:
    p=p*1.1

# La sortie
print(f"Le prix est {p} dh")






