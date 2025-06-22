from Trainee import json_config
from Trainee import ia
from Trainee.terminal import kernel
import asyncio


#Classe principal onde vai criar o "Estagiário"
#Essa classe recebe todas as funções de Kernel
class Trainee(kernel.Kernel):
    def __init__(self, nome : str, personalidade : str, api_key : str, modelo_ia : str = 'gemini-1.5-flash'):
        self.nome = nome
        self.personalidade = personalidade
        self.modelo_ia = modelo_ia
        self.api_key = api_key

        #Precisamos fazer a verificação de modelos depois
        ia.gerar_modelo(api_key, modelo_ia)

        #Atribui oq precisa no Kernel
        super().__init__(self.nome)


        
        #Salva suas configurações em um Json
        json_config.criar_json(self.nome, self.personalidade, self.modelo_ia, self.api_key)
    


    # Onde ele vai obter a resposta da ia 
    #Precisa separa com um if para cada ia que ele pode usar, por enquanto ta so o gemini ent vai essa mesmo
    def _responder(self, prompt : str):
        print(ia.obter_resposta(prompt))
