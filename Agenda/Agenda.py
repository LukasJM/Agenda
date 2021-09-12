from models.My_agenda import Cliente, Agenda
import time



def iniciar_agenda():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    agenda = Agenda()
    print('#############################################')
    print('***  Bem-Vindo a sua agenda de clientes!  ***')
    print('#############################################')
    time.sleep(1.5)
    ola = int(input('Digite uma função:\n'
                '1 Para adicionar um novo cliente a agenda.\n'
                '2 - Para imprimir a agenda completa.\n'
                '3 - Para imprimir os dados de um cliente.\n'
                '4 - Para verificar se um cliente está na agenda.\n'
                '5 - Para verificar os cliente marcados em uma data específica.\n'
                '6 - Para remover um cliente da agenda.\n'
                '7 - Para zerar a data de um cliente.\n'
                '8 - Para informar uma nova data para um cliente.\n'
                '9 - Para sair.\n'))

    if ola == 1:
        nome = input('Informe o nome do cliente:')
        idade = input('Informe a idade do cliente:')
        altura = input('Informe a altura do cliente sem usar vírgula:')
        data = input('Informe uma data para o cliente ser agendado:\n'
                     '*** Por favor, use o formato dd/mm/aaaa ***')

        Agenda.armazena_pessoa(agenda, cli1 := Cliente(nome, idade, altura, data))

        print('Cliente adicionado com sucesso!')
        time.sleep(1)
        print('*** Voltando ao Menu... ***')
        time.sleep(1)
        iniciar_agenda()


    if ola == 2:
        Agenda.imprime_agenda(agenda)
        cont = input('Se deseja voltar ao Menu digite "1", ou digite "0" para sair do programa:')
        if cont == '1':
            iniciar_agenda()
        elif cont == '0':
            print('Fechando agenda...')
            time.sleep(1)
            exit(-1)
        else:
            print('Opção inválida!')
            iniciar_agenda()



    if ola == 3:
        cliente = input('Digite o nome do cliente:')
        Agenda.imprime_cliente(agenda, cliente)
        time.sleep(2)
        cont = input('Se deseja voltar ao Menu digite "1", ou digite "0" para sair do programa:')
        if cont == '1':
            iniciar_agenda()
        elif cont == '0':
            print('Fechando agenda...')
            time.sleep(1)
            exit(-1)
        else:
            print('Opção inválida!')
            iniciar_agenda()


    if ola == 4:
        cliente = input('Digite o nome do cliente:')
        Agenda.busca_pessoa(agenda, cliente)
        time.sleep(2)
        cont = input('Se deseja voltar ao Menu digite "1", ou digite "0" para sair do programa:')
        if cont == '1':
            iniciar_agenda()
        elif cont == '0':
            print('Fechando agenda...')
            time.sleep(1)
            exit(-1)
        else:
            print('Opção inválida!')
            iniciar_agenda()

    if ola == 5:
        data = input('Digite a data no formato "dd/mm/aaaa" por favor:')
        Agenda.buscando_data(agenda, data)
        time.sleep(2)
        cont = input('Se deseja voltar ao Menu digite "1", ou digite "0" para sair do programa:')
        if cont == '1':
            iniciar_agenda()
        elif cont == '0':
            print('Fechando agenda...')
            time.sleep(1)
            exit(-1)
        else:
            print('Opção inválida!')
            iniciar_agenda()

    if ola == 6:
        cliente = input('Digite o nome do cliente a ser removido:')
        Agenda.remover_cliente(agenda, cliente)
        time.sleep(2)
        cont = input('Se deseja voltar ao Menu digite "1", ou digite "0" para sair do programa:')
        if cont == '1':
            iniciar_agenda()
        elif cont == '0':
            print('Fechando agenda...')
            time.sleep(1)
            exit(-1)
        else:
            print('Opção inválida!')
            iniciar_agenda()


    if ola == 7:
        cliente = input('Digite o nome do cliente a ter a data zerada:')
        Agenda.removendo_data_cliente(agenda, cliente)
        time.sleep(2)
        cont = input('Se deseja voltar ao Menu digite "1", ou digite "0" para sair do programa:')
        if cont == '1':
            iniciar_agenda()
        elif cont == '0':
            print('Fechando agenda...')
            time.sleep(1)
            exit(-1)
        else:
            print('Opção inválida!')
            iniciar_agenda()


    if ola == 8:
        cliente = input('Digite o nome do cliente a receber nova data:')
        data = input('Digite a nova data:')
        Agenda.add_data_cliente(agenda, cliente, data)
        time.sleep(2)
        cont = input('Se deseja voltar ao Menu digite "1", ou digite "0" para sair do programa:')
        if cont == '1':
            iniciar_agenda()
        elif cont == '0':
            print('Fechando agenda...')
            time.sleep(1)
            exit(-1)
        else:
            print('Opção inválida!')
            iniciar_agenda()

    if ola == 9:
        print('*** Fechando agenda... ***')
        time.sleep(1)
        exit(-1)

    else:
        print('Opção inváldia! Retornando ao Menu...')
        time.sleep(1.5)
        iniciar_agenda()

    if ola not in lista:
        print('Opção inváldia! Retornando ao Menu...')
        time.sleep(1.5)
        iniciar_agenda()



def main():
    iniciar_agenda()


while True:
    main()