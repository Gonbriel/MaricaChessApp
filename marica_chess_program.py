"""                 Criando o programa para o Clube de Xadrez de Maricá

   1 - Organização de torneios
   2 - Cadastro de jogadores
   3 - Cálculo de rating                                  """



class Palyers():
    def __init__(self, nome, idade, rating, clube):
        self.nome = nome
        self.idade = idade
        self.rating = rating
        self.clube = clube

class Torneios():
    def __init__(self, nome, tipo, data, local):
        self.nome = nome
        self.tipo = tipo
        self.data = data
        self.local = local
