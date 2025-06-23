import pyttsx3
import sounddevice as sd
import numpy as np
import json
from elevenlabs import ElevenLabs

from Trainee import config
from Trainee import log
from Trainee import json_config



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

    arquivo = json_config.ler_configuracao(nome)
    arquivo['Voice']['model'] = "Elevenlabs"
    arquivo["Voice"]['API_VOICE'] = api
    json_config.salvar_arquivo(nome, arquivo)
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
