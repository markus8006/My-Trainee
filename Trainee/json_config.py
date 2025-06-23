#Preciso criar aqui a função para salvar o json
#IMPORTANTE salvar nesta pasta

from Trainee import config
from Trainee import log
import os

import json

# qual pasta vai ficar
pasta = "Trainee\configs"

#verifica se ela existe
os.makedirs(pasta, exist_ok=True)

#Salvas as conf iniciais
def criar_json(nome, personalidade, modeloIA, API_KEY):

    if config.DEBUG:
          log.executando("Criando Json")

    caminho_arquivo = os.path.join(pasta, f"{nome}_config.json")
    configs = {
            'nome' : nome,
            'personalidade' : personalidade,


            'Voice' : 
            {
                'mode' : "False",
                'model' : "None",
                'API_VOICE' : "None"
            },


            'confIA' : 
            
            {
                'Modelo' : modeloIA,
                'API_KEY_IA' : API_KEY

            },  


            'extensao' : 
            [
                '',
            ]
        }

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(configs, arquivo, indent=4, ensure_ascii=False)
            log.sucess(f"Json salvo em {caminho_arquivo}")


#ler algo das config em relação ao nome (A FAZER)
def ler_configuracao(nome : str, config : str) -> str|dict|list:
      'extrai o json u alguma informação dele'

      arquivo = arquivo + '_config.json'