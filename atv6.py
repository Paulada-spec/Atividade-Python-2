# QUESTAO 6
import random

def lancarDado():
    return random.randint(1, 6)

def calcular():
    dado1 = lancarDado()
    dado2 = lancarDado()
    soma = dado1 + dado2
    return soma

lancamentos = int(input("Digite o numero de lancamentos: "))

print(f"Lançando os dados {lancamentos} vezes:")

for i in range(lancamentos):
    soma_dados = calcular()
    print(f"Lançamento {i+1}: Dado 1 = {lancarDado()}, Dado 2 = {lancarDado()}, Soma = {soma_dados}")
