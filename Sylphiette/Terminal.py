import time

class Terminal:
    def __init__(self, bot):
        self.bot = bot
        self.name = bot.getName()
        
    def run(self):  
     
        print(f"\033[1;35m* Welcome to the \033[1m{self.name} Shell\033[0;33m research preview!\033[0m\n")

        print("\033[32;5;208m")
        print(r"""
 _____  _             _    _             _   
/  __ \| |           | |  | |           | |  
| /  \/| |__    __ _ | |_ | |__    ___  | |_ 
| |    | '_ \  / _` || __|| '_ \  / _ \ | __|
| \__/\| | | || (_| || |_ | |_) || (_) || |_ 
 \____/|_| |_| \__,_| \__||_.__/  \___/  \__|                                  
        """)
        print("\033[0m")
        print(f"\033[1;32mBem-vindo ao terminal {self.name}!\033[0m")
        while True:
            print("\n\033[1;34mEscolha uma opção:\033[0m")
            print("1. Rodar programa")
            print("2. Rodar apenas assistente \033[1;36m(PLACEHOLDER)\033[0m")
            print("3. Conversar por texto \033[1;36m(PLACEHOLDER)\033[0m")
            print("4. Sair")
            opcao = int(input("\n\033[1;33mDigite o número da opção: \033[0m"))
            if opcao == 4:
                print("\n\033[1;32mSaindo...\033[0m")
                time.sleep(1)
                break
            elif opcao == 1:
                print("\n\033[1;33mIniciando modelo...\033[0m")
                time.sleep(1)
                self.bot.run()
                
