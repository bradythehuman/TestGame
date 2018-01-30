# Only works with effects that only accept multiplier as a parameter
def increment_primary(effected_unit, effect_str, increment):
    if effect_str in effected_unit.effects:
        effected_unit.effects[effect_str].primary += 1
    else:
        effected_unit.effects[effect_str] = effects_dict[effect_str](increment)


class Effect:
    def __init__(self):
        pass

    def get_primary(self):
        return 0

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
        self.wounds_list = [wound]

    def get_primary(self):
        return len(self.wounds_list)

    def on_update(self, encounter, effected_unit):
        effected_unit.vitality -= sum(self.wounds_list)


class Bleed(Effect):
    def __init__(self):
        self.primary

    def on_round_end(self, encounter, effected_unit):
        self.duation -= 1
        increment_primary(effected_unit, 'BloodLoss', 2 if ThinBlood.duration else 1)


# Effects Bleed
class BloodLoss(Effect):
    def __init__(self, primary):
        self.primary = primary

    def on_update(self, encounter, effected_unit):
        effected_unit.vitality -= self.primary


class Stun(Effect):
    pass


class ThinBlood(Effect):
    def __init__(self):
        self.primary = True

effects_dict = {"BloodLoss": BloodLoss}

