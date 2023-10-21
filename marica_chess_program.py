"""                 Criando o programa para o Clube de Xadrez de Maricá

   1 - Organização de torneios
   2 - Cadastro de jogadores
   3 - Cálculo de rating                                  """

import re

class Players():
    def __init__(self, nome, idade, email, telefone, rating, clube):
        self._nome = nome.title()
        self._idade = idade
        self._email = email
        self._telefone = telefone
        self._rating = rating
        self._clube = clube.upper()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade, int) and nova_idade > 0:
            self._idade = nova_idade
        else:
            raise ValueError('A idade deve ser um número inteiro positivo')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", novo_email):
            self._email = novo_email
        else:
            raise ValueError("O e-mail deve estar em um formato válido.")

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, novo_rating):
        self._rating = novo_rating

    @property
    def clube(self):
        return self._clube

    @clube.setter
    def clube(self, novo_clube):
        self._clube = novo_clube.upper()

    def __str__(self):
        return f'Nome: {self._nome}, Idade: {self._idade}, Rating: {self._rating}, Clube: {self._clube}'

class Torneios():
    def __init__(self, nome, tipo, data, local):
        self._nome = nome
        self._tipo = tipo
        self._data = data
        self._local = local
        self.jogadores = []

    def add_player(self, jogador):
        self.jogadores.append(jogador)

    def delete_player(self, jogador):
        try:
            self.jogadores.remove(jogador)
        except ValueError:
            raise ValueError(f"O jogador {jogador.nome} não está na lista de jogadores deste torneio.")