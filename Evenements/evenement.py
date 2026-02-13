from Evenements.abstractEvenement import AbstractEvenement


class Evenement:
    def __init__(self, evenement: AbstractEvenement):
        self.evenement = evenement

    def executer(self,personnage):
        return self.evenement.executer()
