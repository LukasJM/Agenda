import time
import typing


class Cliente:

    def __init__(self: object, nome: str, idade: int, altura: float, data: str) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__data = data


class Agenda:
    agenda = []

    def armazena_pessoa(self: object, pessoa: object):   # Metodo 1
            self.agenda.append(pessoa)

    def imprime_agenda(self: object):                    # Metodo 2
        print('*** IMPRIMINDO OS DADOS DA AGENDA ***')
        time.sleep(1.5)
        if len(self.agenda) <= 0:
            print('*** Não há cliente cadastrados! ***')
        else:
            for i in self.agenda:
                print(f'Nome: {i._Cliente__nome}| Idade: {i._Cliente__idade} |altura: {i._Cliente__altura}| Data: {i._Cliente__data}|')


    def imprime_cliente(self, cliente):                 # Metodo 3
        for p, i in enumerate(self.agenda):
            if cliente == i._Cliente__nome:
                print('*** IMPRIMINDO OS DADOS DO CLIENTE ***')
                time.sleep(1.5)
                print(
                    f'Dados do Cliente -> Nome: {i._Cliente__nome}| Idade: {i._Cliente__idade} |altura: {i._Cliente__altura}| Data: {i._Cliente__data}|')

            elif cliente != i._Cliente__nome and p == len(self.agenda) - 1:
                print(f'O cliente {cliente} não existe na Agenda.')



    def busca_pessoa(self, nome):                      # Metodo 4
        print('*** VERIFICANDO SE O CLIENTE INFORMADO EXISTE. ***')
        time.sleep(1.5)
        for p, i in enumerate(self.agenda):
            if nome in i._Cliente__nome:
                print('Cliente encontrado!')
                print(
                    f'Dados do Cliente -> Nome: {i._Cliente__nome}| Idade: {i._Cliente__idade} |altura: {i._Cliente__altura}| Data: {i._Cliente__data}|')
            elif nome not in i._Cliente__nome and p == len(self.agenda) - 1:
                print(f'O cliente {nome} não existe na Agenda.')

    def buscando_data(self, data):                     # Metodo 5
        print('*** BUSCANDO CLIENTES NA DATA INFORMADA. ***')
        time.sleep(1.5)
        for p, i in enumerate(self.agenda):
            if data in i._Cliente__data:
                print(
                    f'Clientes na {data} : Nome: {i._Cliente__nome}| Idade: {i._Cliente__idade} |altura: {i._Cliente__altura}|')
            elif data != i._Cliente__data and p == len(self.agenda) - 1:
                 print(f'Não há clientes agendados na data {data}.')



    def remover_cliente(self, nome):                  # Metodo 6
        print('*** REMOVENDO CLIENTE DA AGENDA. ***')
        time.sleep(1.5)
        for i, n in enumerate(self.agenda):
            if nome in n._Cliente__nome:
                print(f'Removendo o contato {n._Cliente__nome}')
                del self.agenda[i]
                print(
                    f'O seguinte Cliente foi removido -> Nome: {n._Cliente__nome}| Idade: {n._Cliente__idade} |altura: {n._Cliente__altura}| Data: {n._Cliente__data}|')
            elif nome != n._Cliente__nome and i == len(self.agenda) - 1:
                print(f'Não há clientes cadastrados com este nome.')



    def removendo_data_cliente(self, cliente):        # Metodo 7

        print('*** ZERANDO A DATA DO CLIENTE. ***')
        time.sleep(1.5)
        for i, n in enumerate(self.agenda):
            if cliente == n._Cliente__nome:
                print(f'Removendo a data do contato {n._Cliente__nome}')
                n._Cliente__data = '0/0/0'
                print(f' A data do Cliente {n._Cliente__nome} está zerada.')
            elif cliente != n._Cliente__nome and i == len(self.agenda) - 1:
                print('Este cliente não existe na agenda.')



    def add_data_cliente(self, cliente: str, data: str):      # Metodo 8

        print('*** DESIGNANDO NOVA DATA AO CLIENTE. ***')
        time.sleep(1.5)
        for i, n in enumerate(self.agenda):
            if cliente == n._Cliente__nome:
                print(f'Alterando a data do cliente {n._Cliente__nome}')
                n._Cliente__data = data
                print(f' A data do Cliente {n._Cliente__nome} foi alterada com sucesso!.')
            elif cliente != n._Cliente__nome and i == len(self.agenda) - 1:
                print('Este cliente não existe na agenda.')



""""# instancia do objeto para Pessoa
cli6 = Cliente('Lukas Mendes', 25, 1.80, '27/03/2021')
cli5 = Cliente('Bob Jack', 32, 1.85, '27/03/2021')
cli4 = Cliente('Billy Joe', 39, 1.89, '07/06/2021')
cli3 = Cliente('Ayn Rand', 69, 1.67, '04/08/2021')
cli2 = Cliente('Thomas Sowell', 85, 1.99, '15/05/2021')
cli1 = Cliente('Hermione Granger', 29, 1.65, '12/05/2021')"""

# instância do objeto para Agenda
#agenda = Agenda()


# Armazenando os dados
"""Agenda.armazena_pessoa(agenda, cli1)
Agenda.armazena_pessoa(agenda, cli2)
Agenda.armazena_pessoa(agenda, cli3)
Agenda.armazena_pessoa(agenda, cli4)
Agenda.armazena_pessoa(agenda, cli5)
Agenda.armazena_pessoa(agenda, cli6)
# adicionando uma variavel com walrus(criar e atribuir ao mesmo tempo)
Agenda.armazena_pessoa(agenda, cli7 := Cliente('Davi Mendes', 27, 1.82, '03/08/2021'))

# testando os comandos
Agenda.imprime_agenda(agenda)

Agenda.remover_cliente(agenda, 'Billy Joe')  # Removendo o contato

Agenda.imprime_cliente(agenda, 'Davi Jonatas')  # Imprimindo pelo nome

Agenda.busca_pessoa(agenda, 'Hermione Granger')  # nome que existe
Agenda.busca_pessoa(agenda, 'Babu Rangel')  # nome não existe na lista

Agenda.buscando_data(agenda, '27/03/2021')   # imprimindo os clientes pela data

Agenda.removendo_data_cliente(agenda, 'Lukas Mendes')
Agenda.imprime_cliente(agenda, 4)

Agenda.add_data_cliente(agenda,'Lukas Mendes', '22/01/2022')
Agenda.imprime_cliente(agenda, 4)"""

