# kernel.py
from Trainee import log
from Trainee.memoria import memoria
import pygetwindow
import pyrect
import os
import re
import asyncio

class Kernel:
    def __init__(self, nome: str):
        self.nome = nome

    async def iniciar_kernel(self):  
        log.sucess(f"Conversação com {self.nome} iniciada:")
        
        while True:
            entrada = input(">> ")
            
            if entrada.lower() == "exit":
                break

            # Lê a memória atual
            with open("Trainee/memoria/memoria.txt", "r", encoding="utf-8") as arquivo:
                memoria_arquivo = arquivo.read()

            # Gera a resposta da IA
            resposta = self._responder(memoria_arquivo + entrada)

            # Salva conversa na memória
            memoria.salvar_na_memoria(entrada, resposta)

            # Executa comandos, se houver
            
            await self.__processar_resposta(resposta)

            # Mostra a resposta
            print("\n" + resposta)
            

    async def __processar_resposta(self, entrada: str) -> None:
        """Procura por comandos no formato [CMD] e executa com os.system().
        Procura por [FALAR], para falar algo
        """

        tarefas = []
        if "[FALAR]" in entrada:
            padrao = r"\[FALAR\](.*?)\[FIM\]"
            trechos = re.findall(padrao, entrada, re.DOTALL)
            for fala in trechos:
                tarefas.append(self.falar(fala))
        if "[CMD]" in entrada:
            padrao_cmd = r"\[CMD\](.*?)\[FIM\]"
            comandos = re.findall(padrao_cmd, entrada, re.DOTALL)
            for cmd in comandos:
                cmd_linha = cmd.strip()
                tarefas.append(self.executar_cmd(cmd_linha))
                log.sucess(f"Comando executado: {cmd_linha}")
        if "[WIN]" in entrada:
            padrao_win = r"\[WIN\](.*?)\[FIM\]"
            comandos = re.findall(padrao_win, entrada, re.DOTALL)
            for win in comandos:
                if "getWindowsWithTitle" in win:
                    pass
                    
                   


        await asyncio.gather(*tarefas)

    
    async def executar_cmd(self, comando : str):
        os.system(comando)
        
