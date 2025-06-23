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
    'Cria o arquivo que será salvo as configurações'

    caminho_arquivo = os.path.join(pasta, f"{nome}_config.json")
    if config.DEBUG:
          log.executando("Criando Json")

    
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



#ler algo das config em relação ao nome 
def ler_configuracao(modelo : str) -> dict:
      caminho = f"Trainee/configs/{modelo}_config.json"
      with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)

def salvar_arquivo(modelo: str, alterações : dict) -> bool:
    caminho = f"Trainee/configs/{modelo}_config.json"
    with open(caminho, 'w', encoding='utf-8') as arquivo:
          json.dump(caminho, alterações, indent=4, ensure_ascii=False)
          return True
      

