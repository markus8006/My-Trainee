from colorama import Fore, init

init(autoreset=True)

def erro(msg : str):
    msg = Fore.RED + msg
    print(msg)

def executando(msg : str):
    msg = Fore.YELLOW + msg
    print(msg)

def sucess(msg : str):
    msg = Fore.GREEN + msg
    print(msg)