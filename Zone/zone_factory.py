from Zone.zone import Zone


class ZoneFactory:
    @staticmethod
    def creer_village():
        return Zone("Village")

    @staticmethod
    def creer_foret():
        return Zone("Foret")

    @staticmethod
    def creer_donjon():
        return Zone("Donjon")