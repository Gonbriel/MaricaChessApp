"""                 Criando o programa para o Clube de Xadrez de Maricá

   1 - Organização de torneios
   2 - Cadastro de jogadores
   3 - Cálculo de rating                                  """

import re, sqlite3

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
        return f'Nome: {self._nome}, Idade: {self._idade}, Rating: {self._rating}, Clube: {self._clube},' \
               f'E-mail: {self.email}'

    def cadastrar_jogador(self):
        conn = sqlite3.connect('jogadores_clube.db')
        cursor = conn.cursor()

        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS jogadores
            (nome TEXT, idade INTEGER,  email TEXT, telefone TEXT, rating REAL, clube TEXT)''')

            cursor.execute('''SELECT * FROM jogadores WHERE nome=? AND clube=?''',
                           (self._nome, self._clube))
            jogador_existente = cursor.fetchone()

            if jogador_existente:
                print(f'O jogador {self._nome} já está cadastrado no clube {self._clube}.')
            else:
                cursor.execute('''INSERT INTO jogadores VALUES(?, ?, ?, ?, ?, ?)''',
                               (self._nome, self._idade, self.email, self._telefone, self._rating, self._clube))

                conn.commit()
                print(f'Jogador {self._nome} cadastrado com sucesso!')
        except Exception as e:
            print(f'Erro ao cadastrar jogador: {e}')
        finally:
            conn.close()

class Torneios():
    def __init__(self, nome, tipo, data, local):
        self._nome = nome
        self._tipo = tipo
        self._data = data
        self._local = local

    def add_player(self, jogador):
        pass

    def delete_player(self, jogador):
        pass