import main
escolha = int(input("Digite o exercicio 1/2 : "))
match escolha:

    case 1:
        print(main.Ex01())
    case 2:
        print(main.Ex02())
    case default:
        print("Erro")
