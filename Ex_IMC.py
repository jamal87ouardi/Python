p=float(input("Entrer le poids en kg: "))
c=int(input("pour entrer la taille en mètres taper 1, pour cm taper 2: "))
t=float(input("Entrer la taille: "))

if c==2 :
    t=t/100

IMC = p/t**2

print(f"IMC vaut {IMC}")