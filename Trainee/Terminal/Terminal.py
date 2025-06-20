


class Kernal:
    def __init__(self, nome):
        self.nome = nome

    def run(self):
        print(f"Terminal {self.nome} iniciado")
        while True:
            entrada = input(">>")
