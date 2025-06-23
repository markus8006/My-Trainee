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

class Voices:

    def __init__(self, nome):
        self.nome = nome
        self.config = json_config.ler_configuracao(nome)
        self.modelo = self.config["Voices"]['model']
        self.api = self.config["Voices"]["API_VOICE"]
        self.engine = None
        self.client = None

        if self.modelo in voices:
            if self.modelo == 'Win':
                pass
            elif self.modelo == 'Elevenlabs':
                pass
    

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
        self.api = nova_api
        self.client = ElevenLabs(api_key=nova_api)
        self.config['Voice']['model'] = "Elevenlabs"
        self.config['Voice']['API_VOICE'] = nova_api
        json_config.salvar_arquivo(self.nome, self.config)
        if config.DEBUG:
            log.sucess("Nova configuração salva")
       
    


    def falar(self, texto: str):

        if self.modo == "Win":
            self.engine.say(texto)
            self.engine.runAndWait()


        elif self.modo == "Elevenlabs":
            

            audio_array = self._run_audio_elevenlabs(texto)
            sd.play(audio_array, samplerate=22050)
            sd.wait()

            if config.DEBUG:
                log.sucess("Áudio reproduzido.")









    def _run_audio_elevenlabs(self, texto):
        if config.DEBUG:
                log.executando("Acessando modelo ElevenLabs...")

        audio = b''.join(
            self.client.text_to_speech.convert(
            text=texto,
            voice_id="qbzdNKUUxcKHZ1WhQ7eX",
            model_id="eleven_multilingual_v2",
            output_format="pcm_22050",
                )
            )
        return np.frombuffer(audio, dtype=np.int16)