import pyttsx3




def conigureVoiceWin(
    voiceId : int = 0, 
    voiceRate : int = 200, 
    voiceVolume : int = 1.0
    ) -> None:
    
  
    global engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voiceId].id)
    engine.setProperty('rate', voiceRate)
    engine.setProperty('volume', voiceVolume)
    
    
def configureVoiceGoogle():
    pass
    
def speakWin(prompt : str) -> None:
    engine.say(prompt)
    engine.runAndWait()
            
if __name__ == "__main__":
    speakWin("Audio funcionando")