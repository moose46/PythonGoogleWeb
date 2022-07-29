class SeriesResistor:
    def __init__(self, list_of_values: {} = None, voltage: float = 0, current: float = 0):
        self.list_of_values = dict()
        if (type(list_of_values) == list):
            x = 1
            for i in list_of_values:
                self.list_of_values[f'R{x}'] = i
                x += 1
        else:
            # print(type(list_of_values))
            self.list_of_values = list_of_values if list_of_values is not None else dict()
        self._voltage = voltage
        self._ohms = self.rT()  # calculate total ohms
        self._current = self.iT() if current == 0 else current  # calculate total current
        self.vS()  # calc the voltage

    def printR(self):
        s = ''
        for k, v in self.list_of_values.items():
            s += k + ' + '
        print(f'{self.__module__}')
        print(f'Rt={s[:-3]} = {self.rT()}\n')
        print([k for k, v in globals().items() if v is self][0])
        print(self)

    def vS(self):
        self._voltage = self._ohms * self._current

    def voltage_drop_across_each_resistor(self):
        print(f"{[k for k, v in globals().items() if v is self][0]} Voltage Drops Vs={self._voltage}V I={self._current:2.3f}A")
        for resistor, v in self.list_of_values.items():
            print(f'\t{resistor} {v} \u03A9 @ {v * self.iT():2.2f}V')

    def rT(self):
        t = 0
        for k, v in self.list_of_values.items():
            # print(k, v)
            t += v
        self._ohms = t
        return t

    def iT(self):
        if self._voltage > 0:
            return self._voltage / self._ohms
        else:
            return 0

    @property
    def ohms(self):
        return self._ohms

    @property
    def voltage(self):
        return self._voltage
    @voltage.setter
    def voltage(self,value):
        self._voltage = value
        self._current = self._voltage / self._ohms

    @property
    def current(self):
        return self._current
    @current.setter
    def current(self,value):
        self._current = value
        self._voltage = self._current * self._ohms

    def pT(self):
        return self._current * self._current * self._ohms

    # @voltage.setter
    # def voltage(self, value):
    #     self._voltage = value

    def __repr__(self):
        s = ''
        for k, v in self.list_of_values.items():
            s += k + ' + '
        return f'Rt={s[:-3]} = {self.rT()}\n' \
               f'Vs= {self._voltage}V\n' \
               f'It= {self._current:2.3f}A\n' \
               f'Pw= {self.pT():2.2f}\n'


r1 = SeriesResistor({'R1': 33, 'R2': 68, 'R3': 100, 'R4': 47, 'R5': 10}, 100)
# # r1.voltage = 10  # 10 volts
print(r1)
# r2 = SeriesResistor({'R1': 4, 'R2': 4}, voltage=30)
# print(r2)
r3 = SeriesResistor([82, 18, 15, 10], 25)
print(r3)
example4_9 = SeriesResistor([1200, 5600, 1200, 1500], voltage=0, current=.001)
example4_9.printR()
# print( [name for name in globals()])
# print( [name for name in locals()])


example4_9 = SeriesResistor([1e3, 3.3e3, 4.7e3], voltage=0, current=1e-3)
example4_9.voltage = 45
example4_9.voltage_drop_across_each_resistor()
example4_9.current = .001
example4_9.voltage_drop_across_each_resistor()
