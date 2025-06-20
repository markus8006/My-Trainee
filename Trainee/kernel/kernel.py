


#Cria a interface, não necessariamente o usuario vai ver 

class Kernel:
    def __init__(self, name : str) -> None:
        self.name = name
        


    #Aqui é onde a ia vai trabalhar, onde vai ter as mensagens e rodar os comandos 
    def run(self) -> None:
        print(f"Kernel Iniciado: {self.name}\n\n")
        while True:
            entrada = str(input(">>"))

        
        