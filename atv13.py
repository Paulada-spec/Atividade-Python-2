# QUESTAO 13
def numOcorrencias(texto):
    palavras = texto.lower().split()
    contador = {palavra: palavras.count(palavra) for palavra in palavras}
    return contador

texto = input("Digite um texto: ")

ocorrencias = numOcorrencias(texto)

print("Ocorrências de cada palavra:")
for palavra, quantidade in ocorrencias.items():
    print(f"{palavra}: {quantidade}")
