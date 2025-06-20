from Trainee import json
from Trainee import IA
from Trainee.Terminal import Terminal
import asyncio


#Classe principal onde vai criar o "Estagiário"
#Essa classe recebe todas as funções de Kernel
class Trainee(Terminal.Kernel):
    def __init__(self, nome : str, personalidade : str, API_KEY : str, modeloIA : str = 'gemini-1.5-flash'):
        self.nome = nome
        self.personalidade = personalidade
        self.modeloIA = modeloIA
        self.API_KEY = API_KEY

        #Precisamos fazer a verificação de modelos depois
        IA.gerarModeloGemini(API_KEY, modeloIA)

        #Atribui oq precisa no Kernel
        super().__init__(self.nome, self)

        
        #Salva suas configurações em um Json
        json.criarJson(self.nome, self.personalidade, self.modeloIA, self.API_KEY)
    


    # Onde ele vai obter a resposta da ia 
    #Precisa separa com um if para cada ia que ele pode usar, por enquanto ta so o gemini ent vai essa mesmo
    def responder(self, prompt : str):
        print(IA.getResponseGemini(prompt))
