from colorama import Fore, init

init(autoreset=True)

def error(msg : str) -> str:
    msg = Fore.RED + msg
    return msg