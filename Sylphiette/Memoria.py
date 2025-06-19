def saveChatMemo(IAname : str, falaIA : str, falaUse :  str, debug : bool =True) -> bool: 
    try:
        try: 
            with open("TempMemo.txt", "x", encoding="utf-8") as arquivo:
                pass
        except:
            pass

        with open("TempMemo.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"User : {falaUse}\n{IAname} : {falaIA}\n")
            return True
    except Exception as e:
        return False, e

def clearMemo(arquivo : str) -> bool:
    
    try:
        with open(arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("")
            return True
    except Exception as e:
        return False, e
    
def readMemo(arquivo : str) -> str:

    with open(arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        return conteudo
    
def saveChatSetup(setup : str) -> bool:
    try:
        try: 
            with open("TempMemo.txt", "x", encoding="utf-8") as arquivo:
                pass
        except:
            pass

        with open("TempMemo.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(setup)
            return True
    except Exception as e:
        return False, e