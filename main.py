from colorama import init, Fore
import time

from Adaptercep import Adaptercep


def main():
    option = 'S'
    while option == 'S':
        # Inicializa o módulo colorama
        init(autoreset=True)

        # Imprime a mensagem de boas-vindas em verde
        print(Fore.GREEN + "Boas vindas ao BuscaCep!")
        time.sleep(1)  # Intervalo de 1 segundo

        # Solicita o CEP ao usuário
        cep = input(Fore.YELLOW + "Digite o CEP que deseja buscar <UM CEP VALIDO CONTÉM 8 DIGITOS>: ")
        time.sleep(0.5)  # Intervalo de 1 segundo

        # Imprime o CEP digitado pelo usuário em azul
        print(Fore.BLUE + "Você digitou o CEP:", cep)
        time.sleep(0.8)  # Intervalo de 1 segundo

        print("Carregando...", end="")
        time.sleep(0.5)  # Intervalo de 0.5 segundos
        print(".", end="")
        time.sleep(0.5)  # Intervalo de 0.5 segundos
        print(".", end="")
        time.sleep(0.5)  # Intervalo de 0.5 segundos
        print(".", end="")
        time.sleep(0.5)  # Intervalo de 0.5 segundos
        print()

        Adaptercep(cep)
        time.sleep(1)  # Intervalo de 1 segundo

        # Solicita ao usuário se deseja continuar e trata erros de entrada
        while True:
            option = input("Deseja continuar? (S/N): ").upper()
            if option in ['S', 'N']:
                break
            print("Opção inválida. Por favor, digite S para continuar ou N para parar.")

        time.sleep(1)  # Intervalo de 1 segundo


if __name__ == '__main__':
    main()