# QUESTAO 7
def fatorial(numero):
    if numero < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    
    elif numero == 0:
        return 1
    
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero = input("Digite um numero: ")

resultado_fatorial = fatorial(numero)

print(f"O fatorial de {numero} é: {resultado_fatorial}")
