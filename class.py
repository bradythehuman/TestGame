class Ability:
    pass


class Item:
    pass


class Minion:
    default_vitality = 0
    default_defense = 0
    cost = 0
    default_abilities = {}
    unit_type = 'basic'
    hero = False

    def __init__(self, xy_pos, unit_id):
        self.xyPos = xy_pos
        self.unit_id = unit_id

        self.vitality = self.default_vitality
        self.defense = self.default_defense
        self.abilities = self.default_abilities

        self.effects = []

    def update_effects(self):
        pass


class Hero:
    def __init__(self):
        pass


class Encounter:
    # Stores all aspects about the current battle including the map, turn order, unit locations, objects on map

    def __init__(self):
        self.map = 0
        self.created_units = 0
        self.units = {}

    def spawn_minion(self, xy_pos):
        self.created_units += 1
        self.units[str(self.created_units)] = Minion(xy_pos)

# class GUI:
#     def __init__(self):
#         pass
#
#     def print_screen(self):
#         pass

