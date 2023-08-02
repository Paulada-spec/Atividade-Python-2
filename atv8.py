# QUESTAO 8
def encontrarPalavra(listaPalavras):
    if not listaPalavras:
        return None, None  
    maiorPalavra = menor_palavra = listaPalavras[0]
    for palavra in listaPalavras:
        if len(palavra) > len(maiorPalavra):
            maiorPalavra = palavra
        elif len(palavra) < len(menorPalavra):
            menorPalavra = palavra
    return maiorPalavra, menorPalavra


listaPalavras = input("Digite uma lista de palavras separadas por espaço: ").split()
maior, menor = encontrarPalavra(listaPalavras)

if maior and menor:
    print(f"A maior palavra é '{maior}' e a menor palavra é '{menor}'.")
else:
    print("A lista está vazia. Nenhuma palavra foi informada.")
