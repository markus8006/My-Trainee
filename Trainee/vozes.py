import pyttsx3
import sounddevice as sd
import numpy as np
from elevenlabs import ElevenLabs
import asyncio

from Trainee import config
from Trainee import log
from Trainee import json_config



# Lista com as vozes possiveis 
voices = [
    "Win"
    "Elevenlabs"
]

class Voices:

    def __init__(self, nome):
        if config.DEBUG:
            log.executando("Iiniciando classe voices")
        self.nome = nome
        self.config = json_config.ler_configuracao(nome)
        self.modelo = self.config["Voice"]['model']
        self.api = self.config["Voice"]["API_ELEVEN"]
        self.engine = None
        self.client = None
        

        if self.modelo in voices:
            if self.modelo == 'Win':
                pass
            elif self.modelo == 'Elevenlabs':
                self._init_elevenlabs()
                self.configurar_elevenlabs()
        if config.DEBUG:
            log.sucess("classe voices iniciada")
    

    def _init_elevenlabs(self):
        if config.DEBUG:
            log.executando('Acessando client Elevenlabs...')
        self.client = ElevenLabs(api_key=self.api)
        if config.DEBUG:
            log.sucess("Client criado")




    def configurar_elevenlabs(self, nova_api : str, 
                              voice_id = "qbzdNKUUxcKHZ1WhQ7eX", 
                              model_id = "eleven_multilingual_v2"):
        
        'configura os elementos do elevenlabs'


        self.voice_id = voice_id
        self.model_id = model_id
        self.api = nova_api
        self.config['Voice']['model'] = "Elevenlabs"
        self.config['Voice']['API_ELEVEN'] = self.api
        self.config['Voice']['voice_id'] = self.voice_id
        self.config['Voice']['modelo_id'] = self.model_id
        json_config.salvar_arquivo(self.nome, self.config)
        self.client = ElevenLabs(api_key=self.api)
        if config.DEBUG:
            log.sucess("Nova configuração salva")
       
    


    async def falar(self, texto: str):
        if self.modelo == "Win":
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, self._falar_win, texto)

        elif self.modelo == "Elevenlabs":
            audio_array = self._run_audio_elevenlabs(texto)
            sd.play(audio_array, samplerate=22050)
            await asyncio.sleep(len(audio_array) / 22050)

            if config.DEBUG:
                log.sucess("Áudio reproduzido.")

    def _falar_win(self, texto):    
        self.engine.say(texto)
        self.engine.runAndWait()

        









    def _run_audio_elevenlabs(self, texto):
        if config.DEBUG:
                log.executando("Acessando modelo ElevenLabs...")

        audio = b''.join(
            self.client.text_to_speech.convert(
            text=texto,
            voice_id=self.voice_id,
            model_id=self.model_id,
            output_format="pcm_22050",
                )
            )
        return np.frombuffer(audio, dtype=np.int16)