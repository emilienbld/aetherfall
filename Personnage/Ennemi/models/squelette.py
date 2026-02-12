from Personnage.Ennemi.ennemi import Ennemi

class Squelette(Ennemi):
    def __init__(self, nom):
        super().__init__(nom=nom, pv=100, attaque=15, defense=20, vitesse=10, agilite=10, endurance=10)