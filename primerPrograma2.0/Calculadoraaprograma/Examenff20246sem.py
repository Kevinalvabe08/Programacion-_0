import random
import os

class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def validarNumero(self, numero):
        self.intentos += 1
        if numero < self.numero_secreto:
            return "No te rindas, es más alto."
        elif numero > self.numero_secreto:
            return "Ya casi, es más bajo."
        else:
            return "¡Esa es, qué grande!"

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def registrarPartida(self, intentos, gano):
        self.historial.append((intentos, gano))

    def estadisticas(self):
        partidas_jugadas = len(self.historial)
        aciertos = sum(1 for _, gano in self.historial if gano)
        porcentaje_aciertos = (aciertos / partidas_jugadas * 100) if partidas_jugadas > 0 else 0
        return partidas_jugadas, porcentaje_aciertos

    def guardarHistorial(self):
        with open('estadisticas.txt', 'w') as f:
            for intentos, gano in self.historial:
                f.write(f"{intentos},{gano}\n")

    def cargarHistorial(self):
        if os.path.exists('estadisticas.txt'):
            with open('estadisticas.txt', 'r') as f:
                for line in f:
                    intentos, gano = line.strip().split(',')
                    self.historial.append((int(intentos), gano == 'True'))


def main():
    nombre = input("Ingresa tu nombre: ")
    jugador = Jugador(nombre)
    jugador.cargarHistorial()

    while True:
        print("\nPantalla de inicio:")
        print("x: Vamos :)")
        print("h: Historial de intentos")
        print("z: Abandonar")
        opcion = input("Selecciona qué opción deseas: ")

        if opcion == 'x':
            juego = JuegoAdivinanza()
            while True:
                try:
                    adivinanza = int(input("Adivina el número secreto que está entre 1 y 100: "))
                    resultado = juego.validarNumero(adivinanza)
                    print(resultado)
                    if resultado == "¡Esa es, qué grande!":
                        jugador.registrarPartida(juego.intentos, True)
                        print(f"¡Eres increíble, lo lograste en {juego.intentos} intentos!")
                        break
                except ValueError:
                    print("Bro? Ese número no es válido. (recuerda que son números del 1 al 100)")

        elif opcion == 'h':
            partidas_jugadas, porcentaje_aciertos = jugador.estadisticas()
            print(f"\nTu historial de partidas {jugador.nombre}:")
            print(f"Partidas Realizadas: {partidas_jugadas}")
            print(f"Tu porcentaje de aciertos: {porcentaje_aciertos:.2f}%")

        elif opcion == 'z':
            jugador.guardarHistorial()
            print("Te extrañaré :(... vuelve pronto....")
            break

if __name__ == "__main__":
    main()