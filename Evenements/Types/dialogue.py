from Evenements.abstractEvenement import AbstractEvenement

class Dialogue(AbstractEvenement):
    def __init__(self, texte):
        self.texte = texte

    def executer(self,personnage):
        return self.texte