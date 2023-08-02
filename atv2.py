# QUESTAO 2
def CalculoMedia(listaNum):
    if not listaNum:
        return 0 
    total = sum(listaNum)
    media = total / len(listaNum)
    return media

numeros = [10, 20, 30, 40, 50]
resultadoMedia = CalculoMedia(numeros)
print("A média dos números é:", resultadoMedia)
