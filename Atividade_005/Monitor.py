class Monitor:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho
        self.computador_conectado = None

    def conectar_computador(self, computador):
        self.computador_conectado = computador

    def desconectar_computador(self):
        self.computador_conectado = None


class Computador:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.monitor = None

    def conectar_monitor(self, monitor):
        self.monitor = monitor
        monitor.conectar_computador(self)

    def desconectar_monitor(self):
        if self.monitor:
            self.monitor.desconectar_computador()
            self.monitor = None

if __name__ == "__main__":
    monitor1 = Monitor("Acer", "Predator")
    computador1 = Computador("Dell", "G15 light")

    computador1.conectar_monitor(monitor1)

    print(f"O monitor conectado ao computador é da marca {computador1.monitor.marca} e possui {computador1.monitor.tamanho}.")

    computador1.desconectar_monitor()

    if computador1.monitor is None:
        print("O monitor foi desconectado do computador.")

    monitor2 = Monitor("LG", "80 polegadas")
    print(f"Monitor independente: {monitor2.marca} - {monitor2.tamanho}.")