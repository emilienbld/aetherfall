from Personnage.Ennemi.models.boss import Boss
from Personnage.Ennemi.models.champion_corrompu import ChampionCorrompu
from Personnage.Ennemi.models.squelette import Squelette
from Personnage.Ennemi.models.bandit import Bandit
from Personnage.Ennemi.models.loup_sauvage import LoupSauvage


class HerosFactory:
    @staticmethod
    def create_hero(hero, name):
        if hero == 'squelette':
            return Squelette()
        if hero == 'bandit':
            return Bandit()
        if hero == 'loup sauvage':
            return LoupSauvage()
        if hero == 'champion corrompu':
            return ChampionCorrompu()
        if hero == 'boss':
            return Boss()
        raise ValueError("Unknown gift type")