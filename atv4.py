# QUESTAO 4
def palind(palavra):
    palavra = palavra.lower() 
    palavraInvertida = palavra[::-1] 

    return palavra == palavraInvertida

escrever = input("Digite uma Palavra: ")
if palind(escrever):
    print(f"A palavra '{escrever}' é um palíndromo.")
else:
    print(f"A palavra '{escrever}' não é um palíndromo.")
