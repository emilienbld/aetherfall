from Personnage.personnage import Personnage
from abc import ABC, abstractmethod

class Heros(Personnage, ABC):

    @abstractmethod
    def choisir_action(self,ennemi):
        pass