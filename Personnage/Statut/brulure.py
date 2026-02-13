from Personnage.Statut.statut import Statut


class Brulure(Statut):
    
    def __init__(self,tour,degats):
        super().__init__(tour)
        self.degats = degats