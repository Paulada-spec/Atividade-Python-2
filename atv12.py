# QUESTAO 12
def mediana(lista):
    listaOrdem = sorted(lista)
    meio = len(listaOrdem) // 2

    if len(listaOrdem) % 2 == 1:
        return listaOrdem[meio]
    else:
        return (listaOrdem[meio - 1] + listaOrdem[meio]) / 2

lista = [5, 3, 1, 2, 4]
resultado = mediana(lista)
print("A mediana da lista é:", resultado)
