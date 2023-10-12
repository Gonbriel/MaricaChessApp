"""                 Criando o programa para o Clube de Xadrez de Maricá

   1 - Organização de torneios
   2 - Cadastro de jogadores
   3 - Cálculo de rating                                  """

class Players():
    def __init__(self, nome, idade, email, telefone, rating, clube):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.rating = rating
        self.clube = clube

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Rating: {self.rating}, Clube: {self.clube}'

class Torneios():
    def __init__(self, nome, tipo, data, local):
        self.nome = nome
        self.tipo = tipo
        self.data = data
        self.local = local
        self.jogadores = []

    def add_player(self, jogador):
        self.jogadores.append(jogador)

    def delete_player(self, jogador):
        if jogador in self.jogadores:
            self.jogadores.remove(jogador)
        else:
            print(f"O jogador {jogador.nome} não está na lista de jogadores deste torneio.")

