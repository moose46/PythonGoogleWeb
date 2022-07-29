import math

"""
Vout = Vin x R2/R1 + R2 where R1 + R2 = Rt
Xc = 1/2piFC in Ohms
Z sqrt(r2 + X^2)

"""


class VoltageDivider:
    """equation to calculate the output voltage for two single resistors connected in series"""

    def __init__(self, r1: float, r2: float):
        self.r1: float = r1
        self.r2: float = r2

    def Rt(self):
        """The total resistance of the circuit"""
        return self.r1 + self.r2

    def Vout(self, vin: float) -> float:
        r: float = self.r2 / (self.r1 + self.r2)
        return vin * r


class CapReactance:
    def __init__(self, capacitance: float):
        self.capacitance: float = capacitance

    def Xc(self, freq: float):
        """Return value in ohms"""
        return 1 / (2 * math.pi * freq * self.capacitance)


def impedance(resistance: float, capacitance: float):
    """In Ohms"""
    return math.sqrt(resistance * resistance + capacitance * capacitance)


def series_resistance(r1: float, r2: float):
    return r2 / r1 + r2


# x = VoltageDivider(100, 100)
# for i in range(1, 10):
#     print(f'volts in={i} volts out = {x.Vout(i)}')
#
# y = CapReactance(47e-6) # 47 microfards
def v_out(v_in, x_c, r):
    return v_in * (x_c / (math.sqrt(r * r + x_c * x_c)))


def capacitive_reactance(capacitance: float, frequency: float):
    """

    :param capacitance: im mfd
    :param frequency: hz
    :return: In Ohms
    """
    return (1 / ((2 * math.pi) * frequency * capacitance))


""" https://www.electronics-tutorials.ws/filter/filter_2.html """
for i in range(100, 10100, 100):
    # print(f'{Xc(47e-6,i)}')
    # print(f'{series_resistance(Xc(47e-6, i), 47000)}')
    V_IN = 4
    X_C = capacitive_reactance(459e-9, i)
    print(f'freq={i} Xc={X_C:2.0f} Vout={v_out(V_IN, X_C, 1000):2.3f}V')
    # print(f'{X_C:1}')
