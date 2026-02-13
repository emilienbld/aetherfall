from Personnage.personnage import Personnage

class Ennemi(Personnage):
    def __init__(self,nom):
        super().__init__(nom=nom,pv=100,attaque=15,defense=20,vitesse=10,agilite=10,endurance=10,boss = False)

    def attaquer(self):
        pass

    def esquive(self):
        pass

    def subir(self):
        pass