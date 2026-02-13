from Evenements.abstractEvenement import AbstractEvenement


class Coffre(AbstractEvenement):
    def __init__(self,item):
        self.item = item

    def executer(self,personnage):
        print(f" Tu as trouvé un coffre. Tu obtiens {self.item}")
        personnage.inventaire.ajout_item(self.item)
        return "coffre"