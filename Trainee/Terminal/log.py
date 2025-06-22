from colorama import Fore, init

init(autoreset=True)

def erro(msg : str) -> str:
    msg = Fore.RED + msg
    return msg

def executando(msg : str) -> str:
    msg = Fore.YELLOW + msg
    return msg

def sucess(msg : str) -> str:
    msg = Fore.GREEN + msg
    return msg