import units_mod


class Encounter:
    # Stores all aspects about the current battle including the map, turn order, unit locations, objects on map

    def __init__(self):
        self.map = 0
        self.created_units = 0
        self.units = {}

    def spawn_minion(self, xy_pos):
        self.created_units += 1
        self.units[str(self.created_units)] = units_mod.Minion(xy_pos, self)


# class GUI:
#     def __init__(self):
#         pass
#
#     def print_screen(self):
#         pass

if __name__ == "__main__":
    current_encounter = Encounter
    current_encounter.spawn_minion(current_encounter, "xyPos")
