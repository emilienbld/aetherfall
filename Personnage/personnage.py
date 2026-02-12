from abc import ABC, abstractmethod


class Personnage(ABC):
    def __init__(self,nom,pv,attaque,defense,vitesse,agilite,endurance):
        self.nom = nom
        self.pv = pv
        self.pvMax = pv
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse
        self.agilite = agilite
        self.endurance = endurance
        self.enduranceMax = endurance

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def subir(self):
        pass

    @abstractmethod
    def esquive(self):
        pass