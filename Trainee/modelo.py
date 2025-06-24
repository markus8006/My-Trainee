from Trainee import json_config
from Trainee import ia
from Trainee import vozes
from Trainee import config
from Trainee.terminal import kernel
from Trainee import log
import asyncio
from Trainee.memoria import memoria

global seguranca


#Classe principal onde vai criar o "Estagiário"
#Essa classe recebe todas as funções de Kernel
class Trainee(kernel.Kernel, vozes.Voices):
    'Classe onde tudo será feito, seria a classe principal'
    def __init__(self, nome : str, personalidade : str, api_key : str, modelo_ia : str = 'gemini-1.5-flash'):
        self.nome = nome
        self.personalidade = personalidade
        self.modelo_ia = modelo_ia
        self.api_key = api_key
        memoria.criar_memoria(self.nome, self.personalidade)

        #Precisamos fazer a verificação de modelos depois
        ia.gerar_modelo(api_key, modelo_ia)

        #Atribui oq precisa no Kernel e as vozes
        kernel.Kernel.__init__(self, self.nome)
        vozes.Voices.__init__(self, self.nome)



        
        #Salva suas configurações em um Json
        json_config.criar_json(self.nome, self.personalidade, self.modelo_ia, self.api_key)


        
        
    


    # Onde ele vai obter a resposta da ia 
    #Precisa separa com um if para cada ia que ele pode usar, por enquanto ta so o gemini ent vai essa mesmo
    def _responder(self, prompt : str) -> str:
        'Busca a resposta da ia '
        return ia.obter_resposta(prompt)
        
    
    #Esqueci de alterar isso no json e daqui 8min tenho q dormir 
    def adicionara_voz(self, modelo, api):
        'configura as vozes se for usar'

        if config.DEBUG:
            log.executando("mandando configurar a voz...")
            
        if modelo == 'Elevenlabs':
            self.configurar_elevenlabs(api)
            if config.DEBUG:
                self.falar("Teste funcionando")
                log.sucess("Voz configurada")

