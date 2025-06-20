import google.generativeai as genai

#Todos os modelos que o usuario pode ter
modelos = [
    "Gemini"
]

#Pra mostrar todos os modelos
def todosModelos() -> list:
      return modelos



#PARA O GEMINI

#Cria o modelo
def gerarModeloGemini(api_key, modelo : str = "gemini-1.5-flash") -> bool:
        global model
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(modelo)
        return True

#Obtem a resposta 
def getResponseGemini(prompt : str) -> str:
    response = model.generate_content(prompt)
    return response.text
