import abilities_mod


class Minion:
    default_vitality = 0
    default_defense = 0
    default_abilities = {}
    stunned = 0


    unit_type = 'basic'
    cost = 0
    hero = False
    summoning_fatigue = True

    def __init__(self, xy_pos, encounter):
        # Initialisation of normal variables
        self.xyPos = xy_pos
        self.encounter = encounter
        self.effects = []
        self.rounds_in_play = 0

        # Initialization of variables altered by effects
        self.vitality = self.default_vitality
        self.defense = self.default_defense
        self.abilities = self.default_abilities
        self.blood_loss = 0

        self.update_effects()

    def update_effects(self):
        self.vitality = self.default_vitality
        self.defense = self.default_defense
        self.abilities = self.default_abilities

        for effect in self.effects:
            try:
                for key in self.effects[effect]:
                    self.effects[effect][key].on_update(self.encounter, self)
            except TypeError:
                self.effects[effect].on_update(self.encounter, self)

# class Hero:
#     def __init__(self):
#         pass