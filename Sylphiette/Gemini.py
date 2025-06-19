import google.generativeai as genai

def gerarModelo(modelo : str, api : str) -> None:
        global model
        genai.configure(api_key=api)
        model = genai.GenerativeModel(modelo)
        return True


def getResponse(prompt : str) -> str:
    response = model.generate_content(prompt)
    return response.text