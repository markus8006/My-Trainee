#Preciso criar aqui a função para salvar o json
#IMPORTANTE salvar nesta pasta

import os

import json

# qual pasta vai ficar
pasta = "Trainee\configs"

#verifica se ela existe
os.makedirs(pasta, exist_ok=True)

#Salvas as conf iniciais
def criar_json(nome, personalidade, modeloIA, API_KEY):
    caminho_arquivo = os.path.join(pasta, f"{nome}_config.json")
    configs = {
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

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(configs, arquivo, indent=4, ensure_ascii=False)

#ler algo das config em relação ao nome (A FAZER)
def ler_configuracao(nome : str, config : str) -> str|dict|list:
      arquivo = arquivo + '_config.json'