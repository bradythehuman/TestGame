order_of_effects = []


class SkillTree:
    def __init__(self):


class Minion:
    default_vitality = 0
    default_defense = 0
    default_abilities = []

    unit_type = 'basic'
    cost = 0
    hero = False
    summoning_fatigue = True

    def __init__(self, xy_pos, encounter):
        # Initialisation of normal variables
        self.xy_pos = xy_pos
        self.encounter = encounter
        self.effects = {}
        self.rounds_in_play = 0

        # Initialization of variables altered by effects
        self.vitality = self.default_vitality
        self.defense = self.default_defense
        self.abilities = self.default_abilities

        self.update_effects()

    def update_effects(self):
        self.vitality = self.default_vitality
        self.defense = self.default_defense
        self.abilities = self.default_abilities

        trimmed_effects = {}
        for key in self.effects:
            if self.effects[key].get_primary():
                trimmed_effects[key] = self.effects[key]
        self.effects = trimmed_effects

        for effect in self.effects:
            self.effects[effect].on_update(self.encounter, self)


class Dan(Minion):
    default_abilities = 7
    default_defense = 2
    default_abilities = []

    unit_type = 'Dan'
    cost = 4

    def a_disaproving_look(self):
