# QUESTAO 5
def NumPares(listaNum):
    NumPares = [numero for numero in listaNum if numero % 2 == 0]
    return NumPares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listaPares = NumPares(lista)

print("Lista original:", lista)
print("Números pares:", listaPares)
