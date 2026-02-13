from Evenements.Types.coffre import Coffre
from Evenements.Types.combat import Combat
from Evenements.Types.dialogue import Dialogue


class EvenementFactory:
    @staticmethod
    def creer_factory_village():
        return [
            Coffre(),
            Dialogue()
        ]

    @staticmethod
    def creer_factory_foret(zone):
        evenements = []

        for ennemi in zone.ennemis:
            event = Combat(ennemi)
            evenements.append(event)

        evenements.extend([
            Coffre(),
            Dialogue()
        ])
        return evenements

    @staticmethod
    def creer_factory_donjon(zone):
        evenements = []

        for ennemi in zone.ennemis:
            event = Combat(ennemi)
            evenements.append(event)

        evenements.extend([
            Coffre(),
            Dialogue()
        ])
        return evenements

    @staticmethod
    def creer_boss_donjon(zone):
        return Combat(zone.boss)