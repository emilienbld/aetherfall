from Personnage.Statut.statut import Statut

class Poison(Statut):

    def __init__(self,tour,degats):
        super().__init__(tour)
        self.degats = degats
