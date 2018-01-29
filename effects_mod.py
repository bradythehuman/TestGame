

def incmt_cont_var(effected_unit, incriment):
    if "BloodLoss" in effected_unit.effects:
        effected_unit.effects["BloodLoss"].multiplier += 1
    else:
        effected_unit.effects["BloodLoss"] = effects_dict["BloodLoss"](incriment)


class Effect:
    def __init__(self):
        self.duration = 0
        self.multiplier = 0

    def on_round_end(self, encounter, effected_unit):
        pass

    def on_damage(self, encounter, effected_unit):
        pass

    def on_ability(self, encounter, effected_unit):
        pass

    def on_update(self, encounter, effected_unit):
        pass

    def description(self):
        return 'This is the Effect class. A framework for all other effects'


class PhysicallyWound(Effect):
    def __init__(self, wound):
        self.duration = 1
        self.wounds_list = [wound]

    def on_update(self, encounter, effected_unit):
        effected_unit.vitality -= sum(self.wounds_list)


class Bleed(Effect):
    def __init__(self, duration, multiplier=1):
        self.duration = duration
        self.multiplier = multiplier

    def on_round_end(self, encounter, effected_unit):
        self.duation -= 1


class BloodLoss(Effect):
    def __init__(self, multiplier):
        self.duration = 1
        self.multiplier = multiplier

    def on_update(self, encounter, effected_unit):
        effected_unit.vitality -= self.multiplier


class Stun:
    pass

effects_dict = {"BloodLoss": BloodLoss}
