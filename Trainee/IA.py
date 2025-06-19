import google.generativeai as genai

modelos = [
    "Gemini"
]

#
def todosModelos() -> list:
      return modelos


def gerarModeloGemini(api_key, modelo : str = "gemini-1.5-flash") -> bool:
        global model
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(modelo)
        return True

def getResponseGemini(prompt : str) -> str:
    response = model.generate_content(prompt)
    return response.text
