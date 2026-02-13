from Personnage.Statut.statut import Statut

class Bouclier(Statut):

    def __init__(self,tour,defense):
        super().__init__(tour)
        self.defense = defense
