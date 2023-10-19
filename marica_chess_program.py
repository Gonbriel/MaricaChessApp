"""                 Criando o programa para o Clube de Xadrez de Maricá

   1 - Organização de torneios
   2 - Cadastro de jogadores
   3 - Cálculo de rating                                  """

class Players():
    def __init__(self, nome, idade, email, telefone, rating, clube):
        self._nome = nome.title()
        self._idade = idade
        self._email = email
        self._telefone = telefone
        self._rating = rating
        self._clube = clube

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
        if jogador in self.jogadores:
            self.jogadores.remove(jogador)
        else:
            print(f"O jogador {jogador.nome} não está na lista de jogadores deste torneio.")

