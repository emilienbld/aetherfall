from Evenements.abstractEvenement import AbstractEvenement


class Coffre(AbstractEvenement):
    def __init__(self,item):
        self.item = item

    def executer(self,personnage):
        print(f" COFFRE trouvé ! Tu obtiens {self.item}")
        personnage.inventaire.ajout_item(self.item)
        return "coffre"