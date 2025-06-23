import google.generativeai as genai

from Trainee import config
from Trainee import log

#Todos os modelos que o usuario pode ter
modelos = [
    "Gemini"
]

#Pra mostrar todos os modelos
def todos_modelos() -> list:
      'lista todos os modelos que se pode usar '
      return modelos



#PARA O GEMINI

#Cria o modelo
def gerar_modelo(api_key, modelo : str) -> bool:
        'Cria o modelo de ia que será usado'
        global model

        #Para gemini
        if config.DEBUG:
              log.executando("Criando modelo gemini...")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(modelo)
        if config.DEBUG:
              log.sucess("Modelo criado")
        return True

#Obtem a resposta 
def obter_resposta(prompt : str) -> str:
    'obtem a resposta da ia'
    if config.DEBUG:
          log.executando("Obtendo resposta...")
    respostas = model.generate_content(prompt)
    if config.DEBUG:
          log.sucess("Resposta obtida")
    return respostas.text
