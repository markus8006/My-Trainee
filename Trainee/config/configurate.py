import json

base = {
    'name' : None,
    'personality' : None,
    'memory' : None,

    'ai' : {
        'api' : None,
        'model' : None,
        'sub_model' : None,
    },

    'voice' : {
        'activated' : False,
        'model' : None,
        'api' : None,
        'voice_id': None,
        'model_id' : None

    },

    'extencions' : [

    ],
}





class Config:
    'Ordena tudo que precisa para salvar configurações'
    def __init__(self, name : str):
        self.name = name
