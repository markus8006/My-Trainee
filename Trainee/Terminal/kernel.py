from . import log
import os


seguranca = 'Você é uma assistente que pode responder perguntas normalmente, mas também pode executar comandos no terminal do Windows.Se o usuário fizer um pedido como "abrir bloco de notas", "mostrar arquivos", "mudar a cor do terminal", ou qualquer comando relacionado ao CMD ou PowerShell, gere um comando dentro da tag especial:[CMD] comando_aquiUse apenas comandos **seguros**, visuais e que possam ser rodados com `os.system("start cmd /k comando")`.Exemplos válidos:- [CMD] start notepad- [CMD] dir- [CMD] color 0A- [CMD] title Sylphiette- [CMD] start cmd /k clsNunca execute comandos perigosos como `del`, `format`, `shutdown`, `reg delete`, etc. Apenas comandos visuais e úteis.Responda primeiro com uma explicação curta do que o comando faz, e em seguida o comando `[CMD]`.Exemplo de resposta:Claro! Isso vai abrir o bloco de notas:[CMD] start notepad'

def alterar_caminho(nome, rota):
    return f"{nome}/{rota}/"


class Kernel:
    def __init__(self, nome : str):
        self.nome = nome
        self.rotas = {
        '/home' : self.__pagina_home,
        '/ia' : self.__pagina_ia,
        }
        self.caminho_atual = '/home/'


    def iniciar_kernel(self):  
        self.__exibir_menu()


    def __exibir_menu(self):
        print(f"""            
Modelo: {self.nome}
Pagina atual: {self.caminho_atual}
              """)
        
        while True:
            entrada = input(f"{self.nome + self.caminho_atual}")
            if entrada == "exit":
                break
            self.__processar(entrada)



    def __pagina_home(self):
        self.caminho_atual = alterar_caminho(self.nome, 'home')





    def __pagina_ia(self):
        comandos = {
            '.'
        }
        self.caminho_atual = alterar_caminho(self.nome, 'ia')
        log.sucess(f"Conversação com {self.nome} iniciada:")
        while True:
            entrada = input(">>")
            
            if entrada == "exit":
                break
            elif self.__processar(entrada):
                break
            else:
                with open("Trainee/memoria/memoria.txt", "r", encoding="utf-8") as arquivo:
                    memoria = arquivo.read()
                resposta = self._responder(memoria + entrada)
                self.__processar_resposta(resposta)
                print("\n" + resposta)










    def __processar(self, entrada : str) -> bool:
        if entrada.startswith("/"):
            if entrada in self.rotas.keys():
                self.rotas[entrada]()
                
            return True
        
        else: 
            return False
        
    def __processar_resposta(self, entrada : str) -> None:
        if "[CMD]" in entrada:
            comando = entrada.split("[CMD]", 1)[1].strip()
             # Remove quebras de linha extras
            comando = comando.splitlines()[0].strip()
            print(comando)
            os.system(comando)
            log.sucess("COMANDO")
    
