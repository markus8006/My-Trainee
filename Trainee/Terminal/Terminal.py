

class Kernel:
    def __init__(self, nome, obj):
        self.nome = nome
        self.obj = obj

    def run(self):
        print(f"Terminal {self.nome} iniciado")
        while True:
            entrada = input(">>")
            self.interpretar(entrada)
               
    def runIA(self):
        while True:
            prompt = input(">>>")
            if prompt == 'exit':
                break
            self.obj.responder(prompt)



    def interpretar(self, msg):
        if msg == "run":
            self.runIA()

