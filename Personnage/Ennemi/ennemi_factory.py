from Personnage.Ennemi.models.boss import Boss
from Personnage.Ennemi.models.champion_corrompu import ChampionCorrompu
from Personnage.Ennemi.models.squelette import Squelette
from Personnage.Ennemi.models.bandit import Bandit
from Personnage.Ennemi.models.loup_sauvage import LoupSauvage


class EnnemiFactory:
    @staticmethod
    def creer_ennemis_foret():
        return [
            Squelette("Squelette 1"),
            Squelette("Squelette 2"),
            Squelette("Squelette 3"),
            Bandit("Bandit 1"),
            Bandit("Bandit 2"),
            Bandit("Bandit 3"),
            LoupSauvage("Loup Sauvage 1"),
            LoupSauvage("Loup Sauvage 2"),
            LoupSauvage("Loup Sauvage 3"),
        ]