import google.generativeai as genai


class AIClient:
    'Entrega toda as configurações relacionadas a IA sobre o Trainee'
    def __init__(self):
        'Inicia as variaveis gerais'
        self.api_key = 
        self.model = 
        self.sub_model = 

        #Cria o modelo
        self.creat_client()
        


    def get_response(self, msg : str) -> str: 
        'Obtem as respostas da IA'
        pass

    def creat_client(self) -> None:
        'cria e salva o modelo IA'
        if self.model == "Gemini":
            genai.configure(api_key=self.api_key)
            self.client = genai.GenerativeModel(self.sub_model)
        else:
            pass

        
