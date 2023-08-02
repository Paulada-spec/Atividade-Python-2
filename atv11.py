# QUESTAO 11
import random

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

def jogo():
    resposta = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1

        if tentativa < resposta:
            print("Tente um número maior.")
        elif tentativa > resposta:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {resposta} em {tentativas} tentativas.")
            break

jogo()
