# from Personnage.Ennemi.models.boss import Boss
# from Personnage.Ennemi.models.champion_corrompu import ChampionCorrompu
# from Personnage.Ennemi.models.squelette import Squelette
# from Personnage.Ennemi.models.bandit import Bandit
# from Personnage.Ennemi.models.loup_sauvage import LoupSauvage


# class EnnemiFactory:
#     @staticmethod
#     def creer_ennemis_foret():
#         return [
#             Squelette("Squelette 1"),
#             Squelette("Squelette 2"),
#             Squelette("Squelette 3"),
#             Bandit("Bandit 1"),
#             Bandit("Bandit 2"),
#             Bandit("Bandit 3"),
#             LoupSauvage("Loup Sauvage 1"),
#             LoupSauvage("Loup Sauvage 2"),
#             LoupSauvage("Loup Sauvage 3"),
#         ]

#     @staticmethod
#     def creer_ennemis_donjon():
#         return [
#             ChampionCorrompu("Champion Corrompu 1"),
#             ChampionCorrompu("Champion Corrompu 2"),
#             ChampionCorrompu("Champion Corrompu 3")
#         ]

#     @staticmethod
#     def creer_boss():
#         return Boss("Boss")


from Personnage.Ennemi.ennemi import Ennemi
from Personnage.Ennemi.models.loup_sauvage import LoupSauvage
from Personnage.Ennemi.models.bandit import Bandit
from Personnage.Ennemi.models.squelette import Squelette
from Personnage.Ennemi.models.champion_corrompu import ChampionCorrompu
from Personnage.Ennemi.models.boss import Boss

class EnnemiFactory:
    def creer_ennemi(self, type_ennemi: str) -> Ennemi:
        type_ennemi = type_ennemi.lower()
        if type_ennemi == "loup_sauvage":
            return LoupSauvage()
        if type_ennemi == "bandit":
            return Bandit()
        if type_ennemi == "squelette":
            return Squelette()
        if type_ennemi == "champion_corrompu":
            return ChampionCorrompu()
        if type_ennemi in ("boss", "gardien_donjon"):
            return Boss()
        raise ValueError(f"Type d'ennemi inconnu : {type_ennemi}")
