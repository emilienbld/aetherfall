# from Personnage.Ennemi.ennemi import Ennemi

# class Squelette(Ennemi):
#     def __init__(self, nom):
#         super().__init__(nom=nom, pv=100, attaque=15, defense=20, vitesse=10, agilite=10, endurance=10)

from Personnage.Ennemi.ennemi import Ennemi

class Squelette(Ennemi):
    def __init__(self, nom: str = "Squelette"):
        super().__init__(
            nom=nom,
            pv=90,
            attaque=12,
            defense=18,
            vitesse=7,
            agilite=5,
            endurance=10,
            intelligence=0,
            niveau=1,
        )

    def resistant_degats(self, degats: int):
        return int(degats * 0.7)
