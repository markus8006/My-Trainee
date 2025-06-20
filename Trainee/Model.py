from Trainee import json
from Trainee import IA
from Trainee.Terminal import kernel


#Classe principal onde vai criar o "Estagiário"
class Trainee:
    def __init__(self, nome : str, personalidade : str, modeloIA : str, API_KEY : str):
        self.nome = nome
        self.personalidade = personalidade
        self.modeloIA = modeloIA
        self.API_KEY = API_KEY

        #Atribui ele a um kernel
        self.Kernel = kernel.NewKernel(f"{self.nome}")
        
        #Salva suas configurações em um Json
        json.criarJson(self.nome, self.personalidade, self.modeloIA, self.API_KEY)


    # Onde ele vai obter a resposta da ia 

    #Precisa separa com um if para cada ia que ele pode usar, por enquanto ta so o gemini ent vai essa mesmo
    def Responde(prompt : str):
        print(IA.getResponseGemini(prompt))
