# QUESTAO 3
def numCrescente(numero):
    for i in range(numero + 1):
        print(i)

def main():
        numero = int(input("Digite um número inteiro positivo: "))
        
        if numero < 0:
            print("erro!!!") #Erro se o numero for negativo

        else:
            numCrescente(numero) 

if __name__ == "__main__":
    main()
