class Ordinateur:
    def __init__(self, marque, processeur, stockage, ram):
        self.marque = marque
        self.processeur = processeur
        self.stockage = stockage
        self.ram = ram

    def __str__(self):
        return f" Marque: {self.marque}\n Processeur: {self.processeur}\n Stockage: {self.stockage}\n RAM: {self.ram}"


class Portable(Ordinateur):
    def __init__(self, marque, processeur, stockage, ram, batterie):
        super().__init__(marque, processeur, stockage, ram)
        self.batterie = batterie

    def __str__(self):
        return f"{super().__str__()} \n Batterie: {self.batterie} \n"



class Bureau(Ordinateur):
    def __init__(self, marque, processeur, stockage, ram, carte_graphique):
        super().__init__(marque, processeur, stockage, ram)
        self.carte_graphique = carte_graphique
    
    def __str__(self):
        return f"{super().__str__()} \n Carte graphique: {self.carte_graphique} \n"


# Exemple d'utilisation
PCportable1 = Portable("HP", "Intel i5", "512GB SSD", "8GB RAM", "6-cell")
PCbureau1 = Bureau("Dell", "AMD Ryzen 7", "1TB HDD", "16GB RAM", "NVIDIA GTX 1660")

print(PCportable1)
print(PCbureau1)
