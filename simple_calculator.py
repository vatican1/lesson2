class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value

    def __add__(self, args):
        if isinstance(args, Calculator):
            self.value += args.value
            return self
        else:
            self.value += args
            return self

    def __sub__(self, args):
        if isinstance(args, Calculator):
            self.value -= args.value
            return self
        else:
            self.value -= args
            return self

    def __mul__(self, args):
        if isinstance(args, Calculator):
            self.value *= args.value
            return self
        else:
            self.value *= args
            return self

    def __truediv__(self, args):
        if isinstance(args, Calculator):
            self.value /= args.value
            return self
        else:
            self.value /= args
            return self

    def __pow__(self, power, modulo=None):
        if isinstance(power, Calculator):
            self.value **= power
            return self
        else:
            self.value **= power
            return self

    def __str__(self):
        return str(self.value)


print((Calculator(2) + Calculator(5) - Calculator(6))*Calculator(3)**2/Calculator(3))
