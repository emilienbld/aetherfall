from abc import ABC, abstractmethod


class AbstractEvenement(ABC):

    @abstractmethod
    def executer(self,personnage):
        pass