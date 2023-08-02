# QUESTAO 9
def converter(lista_strings):
    nova = []
    for string in lista_strings:
        nova = lista_strings.upper()
    return nova

lista = input("Digite uma palavra: ")
maiusculas = converter(lista)
print("Lista original:", lista)
print ("Lista em maiúsculas: ", maiusculas)
