import json
import os

class Pessoa:
    DATA_FILE = "data/pessoas.json"

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def to_dict(self):
        return {"nome": self.nome, "cpf": self.cpf}

    @staticmethod
    def salvar_pessoa(pessoa):
        pessoas = Pessoa.carregar_pessoas()
        pessoas.append(pessoa.to_dict())
        Pessoa._salvar_em_arquivo(pessoas)

    @staticmethod
    def carregar_pessoas():
        if not os.path.exists(Pessoa.DATA_FILE):
            return []
        with open(Pessoa.DATA_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def _salvar_em_arquivo(pessoas):
        with open(Pessoa.DATA_FILE, "w") as f:
            json.dump(pessoas, f, indent=4)
