from Sylphiette import Gemini
from Sylphiette import Voices
from Sylphiette import Acessos
from Sylphiette import Terminal
from Sylphiette import Memoria

def conifure_voice(model : str):
    if model == "Win":
        Voices.conigureVoiceWin()
    elif model == "Evenlabs":
        pass



class AI:
    def __init__(
        self, name : str,
        personalidade : str,
        api_key : str, 
        fala = True,
        model_fala : str = "Win",
        model='gemini-1.5-flash',
        debug = False
        ) -> None:
        
        Voices.conigureVoiceWin()
        Memoria.clearMemo("TempMemo.txt")
        self.name = name
        self.personalidade =  f"""
        seu Setup:
        Seu nome: {name}
        Sua personalidade, fale como: {personalidade} 
        Agora fale em tom de conversação
        Inicio do chat:\n"""
        Memoria.saveChatSetup(self.personalidade)
        self.model = model
        self.fala = fala
        self.debug = debug
        self.api = api_key
        Gemini.gerarModelo(model, api_key)
        self.terminal = Terminal.Terminal(self)
            
    def resposta(self, prompt : str) -> str:
        prompt_completo = Memoria.readMemo("TempMemo.txt") + prompt
        if self.debug:
            print(prompt_completo)
        respost = Gemini.getResponse(prompt_completo)
        print(f"\033[1;33m{self.name}: \033[0m" + respost)
        if self.fala:
            Voices.speakWin(respost)          
        Memoria.saveChatMemo(self.name, respost, prompt)
        return respost
    
    def run(self) -> None:
        print(f"""
              \033[1;33mModelo: {self.name}\033[0m

              """)
        while True:
            prompt = input("\033[1;32mUsuario: \033[0m")
            if prompt == "SAIR CHAT":
                break
            print("")
            self.resposta(prompt)
            
    def getName(self) -> str:
        return self.name
            
    def runTerminal(self) -> str:
        self.terminal.run()





def setConfDict(conf : dict) -> bool:
    pass 

def setConf(
    obj             : object,
    nome            : str,
    modelo          : str,
    personalidade   : str,
    apiKey          : str,
    debug           : bool,
    fala            : bool, 
    modelFala       : bool 
                    ) -> None:
     
    conf = [nome, modelo, personalidade, apiKey, debug, fala, modelFala]
    for i in len(conf):
        if conf[i] != None:
            obj.conf[i] = conf[i]
            
    
    setConfDict(conf)