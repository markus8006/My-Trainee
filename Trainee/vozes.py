import pyttsx3
import sounddevice as sd
import numpy as np
import json

from Trainee import config

from Trainee import log
from elevenlabs import ElevenLabs


# Lista com as vozes possiveis 
voices = [
    "Win"
    "Elevenlabs"
]

def configurar_elevenlabs(api, nome):
    'configura os elementos do elevenlabs'

    global client
    if config.DEBUG:
        log.executando("Criando cliente Elevenlabs...")
    client = ElevenLabs(api_key=api)
    if config.DEBUG:
        log.sucess("Client criado")
        log.executando("Salvando mudanças")

    caminho = f"Trainee/configs/{nome}_config.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        arquivo = json.load(arquivo)
        arquivo['Voice']['model'] = "Elevenlabs"
        arquivo["Voice"]['API_VOICE'] = api
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(arquivo, f, indent=4, ensure_ascii=False)
            if config.DEBUG:
                log.sucess("Alteações salvas")

    


def falar(texto: str):
    'usa a fala em audio'
    if config.DEBUG:
        log.executando("Acessando modelo elevenlabs...")
    audio = b"".join(client.text_to_speech.convert(
    text=texto,
    voice_id="qbzdNKUUxcKHZ1WhQ7eX",
    model_id="eleven_multilingual_v2",
    output_format="pcm_22050",
))
    if config.DEBUG:
        log.sucess("Elevenlabs acessado")
    audio_array = np.frombuffer(audio, dtype=np.int16)
    sd.play(audio_array, samplerate=22050)
    sd.wait()
