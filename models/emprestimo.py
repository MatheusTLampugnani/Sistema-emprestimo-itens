import json
import os
from datetime import datetime

class Emprestimo:
    DATA_FILE = "data/emprestimos.json"

    def __init__(self, codigo_item, cpf_pessoa, data, devolvido=False):
        self.codigo_item = codigo_item
        self.cpf_pessoa = cpf_pessoa
        self.data = data
        self.devolvido = devolvido

    def to_dict(self):
        return {
            "codigo_item": self.codigo_item,
            "cpf_pessoa": self.cpf_pessoa,
            "data": self.data,
            "devolvido": self.devolvido
        }

    @staticmethod
    def salvar_emprestimo(emprestimo):
        lista = Emprestimo.carregar_emprestimos()
        lista.append(emprestimo.to_dict())
        Emprestimo._salvar_em_arquivo(lista)

    @staticmethod
    def carregar_emprestimos():
        if not os.path.exists(Emprestimo.DATA_FILE):
            return []
        with open(Emprestimo.DATA_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def atualizar_emprestimos(lista):
        Emprestimo._salvar_em_arquivo(lista)

    @staticmethod
    def _salvar_em_arquivo(lista):
        with open(Emprestimo.DATA_FILE, "w") as f:
            json.dump(lista, f, indent=4)
