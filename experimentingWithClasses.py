class MyFavoriteNumber:
    def __init__(self, number):
        self.number = number

    def set_number(self, target):
        target.number = self.number

    def output(self, multiplier):
        print(self.number * multiplier)


class CurrentNumber:
    def __init__(self):
        self.number = 2

    def output(self):
        print(self.number)


x = CurrentNumber()
method_name = "output"
x.method_name()
