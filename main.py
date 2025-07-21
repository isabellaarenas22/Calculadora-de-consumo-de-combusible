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
            ve = float(input("Velocidad de eyeccion (m/s): "))
            m0 = float(input("Masa inicial (kg): "))
            mf = float(input("Masa final (kg): "))

            # Calculo
            calculadora = RocketCalculator(ve, m0, mf)
            delta_v = calculadora.calcular_delta_v()
            print(f"\n El Delta-V es: {delta_v:.2f} m/s")

        except ValueError as e:
            print(f" Error: {e}")


if __name__ == "_main_":
    Main.run()
import math
import matplotlib.pyplot as plt

class RocketCalculator:
    def __init__(self, ve: float, m0: float, mf: float):
        self.ve = ve
        self.m0 = m0
        self.mf = mf

    def calcular_delta_v(self):
        if self.mf <= 0 or self.m0 <= self.mf:
            raise ValueError("La masa final debe ser mayor que cero y menor que la masa inicial.")
        return self.ve * math.log(self.m0 / self.mf)


class DeltaVPlotter:
    def __init__(self, ve: float, m0: float):
        self.ve = ve
        self.m0 = m0

    def graficar_delta_v_vs_mf(self, mf_min: float = 1000, paso: float = 100):
        mf_values = list(range(int(mf_min), int(self.m0), int(paso)))
        delta_v_values = []

        for mf in mf_values:
            try:
                delta_v = self.ve * math.log(self.m0 / mf)
                delta_v_values.append(delta_v)
            except ValueError:
                delta_v_values.append(0)

        plt.figure(figsize=(8, 5))
        plt.plot(mf_values, delta_v_values, marker='o', linestyle='-', color='blue')
        plt.title('Delta-V vs Masa Final')
        plt.xlabel('Masa final (kg)')
        plt.ylabel('Delta-V (m/s)')
        plt.gca().invert_xaxis()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


class Main:
    @staticmethod
    def run():
        print(" Calculadora de Delta-V")
        try:
            ve = float(input("Velocidad de eyección (m/s): "))
            m0 = float(input("Masa inicial (kg): "))
            mf = float(input("Masa final (kg): "))

            # Calculo
            calculadora = RocketCalculator(ve, m0, mf)
            delta_v = calculadora.calcular_delta_v()
            print(f"\nEl Delta-V es: {delta_v:.2f} m/s")

            # Grafica
            grafico = DeltaVPlotter(ve, m0)
            grafico.graficar_delta_v_vs_mf()

        except ValueError as e:
            print(f" Error: {e}")


if __name__ == "__main__":
    Main.run()


