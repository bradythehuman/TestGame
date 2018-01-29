import effects_mod


def get_target(range_):
    return input('copy unit name and location the return')


def apply_effect(target, effect_str, multiplier=0):
    if not target.effects[effect_str]:
        target.effects[effect_str] = [effects_mod.Wound(multiplier)]
    elif effect_str in ['BloodLoss']:
        target.effects[effect_str][0].multiplier += multiplier
    else:
        target.effects[effect_str].append(effects_mod.Wound(multiplier))


class Ability:
    def __init__(self, cost=0):
        self.cost = cost

    def call_ability(self):
        pass
