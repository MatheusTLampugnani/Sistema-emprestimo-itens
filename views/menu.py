from controllers.controller import Controller

def menu():
    while True:
        print("\n===== SISTEMA DE EMPRÉSTIMO =====")
        print("1 - Cadastrar item")
        print("2 - Cadastrar pessoa")
        print("3 - Registrar empréstimo")
        print("4 - Registrar devolução")
        print("5 - Listar itens")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do item: ")
            codigo = input("Código do item: ")
            Controller.cadastrar_item(nome, codigo)
        elif opcao == "2":
            nome = input("Nome da pessoa: ")
            cpf = input("CPF da pessoa: ")
            Controller.cadastrar_pessoa(nome, cpf)
        elif opcao == "3":
            codigo = input("Código do item: ")
            cpf = input("CPF da pessoa: ")
            Controller.registrar_emprestimo(codigo, cpf)
        elif opcao == "4":
            codigo = input("Código do item: ")
            Controller.registrar_devolucao(codigo)
        elif opcao == "5":
            Controller.listar_itens()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
