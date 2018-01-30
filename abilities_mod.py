import effects_mod


def get_target(range):
    return input('copy unit name and location the return')


def apply_effect(target, effect_str, multiplier=0):
    if not target.effects[effect_str]:
        target.effects[effect_str] = [effects_mod.Wound(multiplier)]
    elif effect_str in ['BloodLoss']:
        target.effects[effect_str][0].multiplier += multiplier
    else:
        target.effects[effect_str].append(effects_mod.Wound(multiplier))


class Ability:
    default_cost = 0
    default_type = 'basic'

    def __init__(self):
        self.cost = self.default_cost
        self.type = self.default_type

    def call_ability(self, caster):
        caster.mana -= self.cost
        self.ability_effect(caster)

    def ability_effect(self, caster):
        pass

