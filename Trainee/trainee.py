from config import configurate
from ai import client

class Trainee():
    def __init__(self, name : str, personality : str):
        self.name = name
        self.personality = personality

        super().__init__()