from Carro import Automovel


def main():
    global distancia
    opcao = 0
    combustivel = 60
    quantidade_combustivel = 10
    consumo = 15
    carro = Automovel(combustivel, quantidade_combustivel, consumo)

    while opcao != 2:
        print("0- Abastecer")
        print(f"1- autonomia")
        print("2- distancia a percorrer")
        print("3- exit")

        opcao = eval(input("-> "))

        if opcao == 0:
           consumo = int(input("introduza a quantidade em litros: "))
        if opcao == 2:
            distancia = int(input("Introduza a distancia: "))
        if opcao == 3:
            return

        test = {
            0: carro.autonomia(),
            1: carro.autonomia(),
            2: carro.percorrer(distancia)
        }
        print(test[opcao])



if __name__ == "__main__":
    main()