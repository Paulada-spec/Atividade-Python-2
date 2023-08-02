# QUESTAO 14
def ordenar(lista):
    return sorted(lista)

entrada = input("Digite uma sequência de números separados por espaço: ")
numeros = [int(x) for x in entrada.split()]

listaOrdenada = ordenar(numeros)
print("Lista original:", numeros)
print("Lista ordenada:", listaOrdenada)
