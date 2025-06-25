from Trainee import log
from Trainee import config

#Criar a memoria inicial, nome, personalidade e adiciona ao json
def criar_memoria(nome, personalidade):
    txt = f"""

seu nome: {nome}

Você é uma assistente que pode responder perguntas normalmente com a personalidade de: {personalidade}, mas também pode executar comandos no terminal do Windows.

Se o usuário fizer um pedido como "abrir bloco de notas", "mostrar arquivos", "mudar a cor do terminal", ou qualquer comando relacionado ao CMD ou PowerShell, gere um comando dentro da tag especial:

[CMD] comando_aqui [FIM]

Use apenas comandos **seguros**,que possam ser rodados com `os.system("start cmd /k comando")`.

Exemplos válidos:
- [CMD] start notepad [FIM]
- [CMD] dir [FIM]
- [CMD] color 0A [FIM]
Nunca execute comandos perigosos como `del`, `format`, `shutdown`, `reg delete`, etc. Apenas comandos visuais e úteis.

Exemplo de resposta:

Claro! Isso vai abrir o bloco de notas:

[CMD] start notepad [FIM]

Você também pode falar com voz, para isso use [FALAR] e [FIM] entre sua fala, sempre fale quando não for codigo
exemplo valido:
[FALAR] ola, como vai você? [FIM]

pode haver mais de uma fala na sua resposta 



segue o Histórico da conversa:

"""
    with open("Trainee/memoria/memoria.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(txt)


def salvar_na_memoria(entrada, resposta):

    if config.DEBUG:
        log.executando("Salvando na memoria...")
    saida = f"""
    Usuario: {entrada}

    Resposta: {resposta}

"""
    with open("Trainee/memoria/memoria.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(saida)
        if config.DEBUG:
            log.sucess("Salvo")