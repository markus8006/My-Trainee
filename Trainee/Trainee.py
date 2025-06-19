import json
from Trainee import IA



class Trainee:
    def __inti__(
            self,
            nome : str,
            personalidade : str,
            modeloIA : str,
            API_KEY : str,
            ):
        
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

    def Responde(prompt : str):
        print(IA.getResponseGemini(prompt))
