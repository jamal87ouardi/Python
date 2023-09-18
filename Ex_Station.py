q=float(input("Entrer la quantité: "))
t=int(input("Choisir entre Diesel (1) ou Essence (2): "))

if t==1 :
    prixTotal = 17*q

else :
    prixTotal = 18*q

if q>=100:
    prixTotal = prixTotal*95/100

print(f"le prix à payer est {prixTotal} dh")