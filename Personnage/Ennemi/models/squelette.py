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
        )

    def resistant_degats(self, degats: int):
        return int(degats * 0.7)
