import json
from Trainee import IA
from Trainee.kernel import kernel


#Classe principal onde vai criar o "Estagiário"
class Trainee:
    def __inti__(
            nome : str, 
            personalidade : str,
            modeloIA : str,
            API_KEY : str,
            self,
            ):
        
        #Atribui ele a um kernel
        self.Kernel = kernel.Kernel(f"{nome}")
        
        #Salva suas configurações em um Json
        self.Trainee = {
            'nome' : nome,
            'personalidade' : personalidade,
            'Voice' : {
                'mode' : "False",
                'model' : "None",
                'API_VOICE' : "None"
            },
            'confIA' : {
                'Modelo' : modeloIA,
                'API_KEY_IA' : API_KEY

            },    
            'extensao' : [
                '',
            ]
        }
        with open(f"config_{nome}.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.Trainee, arquivo, indent=4, ensure_ascii=False)


    # Onde ele vai obter a resposta da ia 

    #Precisa separa com um if para cada ia que ele pode usar, por enquanto ta so o gemini ent vai essa mesmo
    def Responde(prompt : str):
        print(IA.getResponseGemini(prompt))
