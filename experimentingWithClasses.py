def print_number(self):
    print(self.number)


class CurrentNumber:
    def __init__(self):
        self.number = 2

    def output(self, number2):
        print_number(self)
        print(number2)


x = CurrentNumber()
method_name = x.output()
x.output()
