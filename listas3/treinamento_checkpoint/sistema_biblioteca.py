import os

os.system('cls')

opcao = 0

while opcao != 6:
    print("Bem-vindo à Biblioteca FIAP")

    print("1 - Reserva Livro\n2 - Cadastra Livro")
    print("3 - Devolução\n4 - Consulta Livro")
    print("1 - Cadastro do Leitor\n6 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        isdn = int(input("Informe o isdn do livro: "))
        leitor = input("CPF do leitor: ")
        print("Disponivel a partir do dia: 25/04/2024")
        confirmacao = input("Deseja reservar (s/n)")
        
        while confirmacao != "s" and confirmacao !="n":
            print("Opção errada, tente novamente.")
        if confirmacao == "s":
            print("Livro reservado, obrigado!")
        else:
            print("Livro não reservado obrigado")
    elif opcao == 2:
        nome_livro = int(input("Digite o nome do livro: "))
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        nome = input("Digite seu nome: ")
        cpf = input("Informe o CPF:")
        celular = input("Número de telefone: ")
        rm = input("RM: ")



    elif opcao == 6:
        print("Até logo!")
    else:
        print("Opção Inválida!\n")


 
