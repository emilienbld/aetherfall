class Arme():
    def __init__(self,name,degats,element):
        self.name = name
        self.degats = degats
        self.element = element

    def attaqueAvecArme(self, personnage , cible):
        return personnage.attaque + self.degats