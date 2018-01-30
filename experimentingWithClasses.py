def print_number(self, multiplier):
    print(self.number * multiplier)


class CurrentNumber:
    def __init__(self):
        self.number = 2
        self.functions = []

    def output(self, number2):
        print_number(self)
        print(number2)


x = CurrentNumber()
x.functions.append(print_number)
params = (x, 2)
x.functions[0](*params)
