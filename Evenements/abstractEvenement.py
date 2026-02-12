from abc import ABC, abstractmethod


class AbstractEvenement(ABC):

    @abstractmethod
    def excuter(self,personnage):
        pass