
def alterar_caminho(nome, rota):
    return f"{nome}/{rota}/"


class Kernel:
    def __init__(self, nome):
        self.nome = nome
        self.rotas = {
        '/home' : self.__pagina_home,
        '/ia' : self.__pagina_ia,
        }
        self.caminho_atual = '/home'


    def iniciar_kernel(self):  
        self.__exibir_menu()


    def __exibir_menu(self):
        print(f"""            
Modelo: {self.nome}
Pagina atual: {self.caminho_atual}
              """)
        
        while True:
            entrada = input(f"{self.nome + self.caminho_atual}/")
            self.__processar(entrada)


    def __pagina_home(self):
        self.caminho_atual = alterar_caminho(self.nome, 'home')

    def __pagina_ia(self):
        self.caminho_atual = alterar_caminho(self.nome, 'ia')









    def __processar(self, entrada : str):
        if entrada.startswith("/"):
            if entrada in self.rotas.keys():
                self.rotas[entrada]()