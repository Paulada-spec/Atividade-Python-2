# QUESTAO 10
entrada = input("Digite uma sequência de números separados por espaço: ")
numeros = [int(x) for x in entrada.split()]

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
