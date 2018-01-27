class Effect:
    def __init__(self):
        self.duration = 1
        self.multiplier = 0

    def on_round_end(self):
        pass

    def on_damage(self):
        pass

    def on_attack(self):
        pass

    def on_update(self, encounter, unit_id):
        pass


class Wound(Effect):
    def __init__(self, multiplier):
        self.duration = 1
        self.multiplier = multiplier


class Bleed(Effect):
    def __init__(self, multiplier):
        self.duration = multiplier

    def on_round_end(self):
