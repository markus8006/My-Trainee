import pyttsx3
import sounddevice as sd
import numpy as np

from Trainee import config

from Trainee.terminal import log
from elevenlabs import ElevenLabs, play


# Lista com as vozes possiveis 
voices = [
    "Win"
    "Elevenlabs"
]

def adicionar_api_elevenlabs(api):
    global client
    client = ElevenLabs(api_key=api)

from elevenlabs import ElevenLabs, play

# Cria o cliente com sua API
client = ElevenLabs(api_key="SUA_API_KEY")

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
