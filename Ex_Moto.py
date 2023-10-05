
# Les entrées:

marque = input("Entrer la marque: ")
while marque not in ["yamaha","suzuki"]:
     marque = input("Réentrer la marque yamaha/suzuki: ")


cat = input("Entrer la catégorie: ")
while cat not in ["sportif","trail","cross"]:
    cat = input("Réentrer la categorie sportif/trail/cross: ")

ci = input("Client interne true/false: ")
while ci not in ["true","false"]:
       ci = input("Client interne true/false: ")


if marque=="yamaha":
    if cat=="sportif":
        prixTotal = 180000
    else:
        if cat=="trail":
            prixTotal = 200000
        else:
            if cat=="cross":
                prixTotal = 130000
            

else:
    if cat=="sportif":
        prixTotal = 195000
    else:
        if cat=="trail":
            prixTotal = 250000
        else:
            if cat=="cross":
                prixTotal = 150000
            

if ci=="true":
    if marque != "yamaha" or cat != "trail":
        prixTotal = prixTotal * 0.95


# Sortie
print(f"Le total est: {prixTotal} dh ")