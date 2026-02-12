from Personnage.Heros.heros import Heros

class Mage(Heros):
    def __init__(self,nom):
        super().__init__(nom=nom,pv=100,attaque=15,defense=20,vitesse=10,agilite=10,endurance=10,intelligence=10,mana=50,manaMax=50)

    def bouleDeFeu(self):
        pass

    def bouclierArcanique(self):
        pass