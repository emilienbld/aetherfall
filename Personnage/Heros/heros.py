from Personnage.personnage import Personnage

class Heros(Personnage):
    def __init__(self,nom):
        super().__init__(nom=nom,pv=100,attaque=15,defense=20,vitesse=10,agilite=10,endurance=10)

    def attaquer(self,cible):
        pass

    def esquive(self):
        pass

    def subir(self, degats):
        pass