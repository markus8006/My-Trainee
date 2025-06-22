import google.generativeai as genai

#Todos os modelos que o usuario pode ter
modelos = [
    "Gemini"
]

#Pra mostrar todos os modelos
def todos_modelos() -> list:
      return modelos



#PARA O GEMINI

#Cria o modelo
def gerar_modelo(api_key, modelo : str) -> bool:
        global model
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(modelo)
        return True

#Obtem a resposta 
def obter_resposta(prompt : str) -> str:
    respostas = model.generate_content(prompt)
    return respostas.text
