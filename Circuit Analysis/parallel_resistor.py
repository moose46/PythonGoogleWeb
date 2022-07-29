class Resistor:

    def __init__(self, list_of_values: [] = None):
        self.resistors = list_of_values if list_of_values is not None else list()

    def add_parallel_resistor(self, value_ohms: float):
        """Add a resistor to a parallel resistor circuit"""
        self.resistors.append(value_ohms)

    def ohms(self):
        value = 0
        for i in self.resistors:
            value += 1 / i
        return 1 / value
    def series_ohms(self):
        rT = 0
        for i in self.resistors:
            rT += i
        return rT
    def branch_current(self, current):
        total = self.ohms()
        r = 1
        iT = 0
        for i in self.resistors:
            print(f'R{r} {i:8,} Ohms = {total:2.3f} / {i} = {total/i:2.3f}uS')
            r+=1
            iT += total/i
        print(f'Total Ohms = {self.ohms():2.2f} Ohms')
        print(f'Total Current = {iT* current:2.3f} mA')
        print(f'Total Voltage = {current * self.ohms():2.3f} Volts')
        print(f'Total Power = {current*current * self.ohms():2.3f} Watts')

    def __str__(self):
        return f'{self.ohms():2.2f}'

R1 = 1000
R2 = 2200
R3 = 1800
R4 = 330
R5 = 680

r = Resistor([R1,R2])
print(f'{r}')
r = Resistor([R3, R4 + R5])
print(f'{r}')
print(f'{r.series_ohms():2.2f} Ohms')