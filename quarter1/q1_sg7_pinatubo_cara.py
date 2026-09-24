class Glassware:
    def __init__(self):
        self.material = "glass"
        self.is_clean = True


class Beaker(Glassware):
    pass


class Tray:
    def __init__(self):
        self.beakers = []
        for i in range(5):
            self.beakers.append(Beaker())


my_tray = Tray()
del my_tray