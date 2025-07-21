import math
import matplotlib.pyplot as plt

class RocketCalculator:
    def _init_(self, ve: float, m0: float, mf: float):
        self.ve = ve
        self.m0 = m0
        self.mf = mf

    def calcular_delta_v(self):
        if self.mf <= 0 or self.m0 <= self.mf:
            raise ValueError("La masa final debe ser mayor que cero y menor que la masa inicial.")
        return self.ve * math.log(self.m0 / self.mf)


class Main:
    @staticmethod
    def run():
        print("Calculadora de Delta-V")
        try:
            ve = float(input("Velocidad de eyección (m/s): "))
            m0 = float(input("Masa inicial (kg): "))
            mf = float(input("Masa final (kg): "))

            # Cálculo
            calculadora = RocketCalculator(ve, m0, mf)
            delta_v = calculadora.calcular_delta_v()
            print(f"\n✅ El Delta-V es: {delta_v:.2f} m/s")

        except ValueError as e:
            print(f"⚠ Error: {e}")


if _name_ == "_main_":
    Main.run()
