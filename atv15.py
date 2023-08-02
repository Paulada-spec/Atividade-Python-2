# QUESTAO 15
def celsiusFahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheitFelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Escolha a conversão:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

escolha = int(input("Digite o número da opção desejada: "))

if escolha == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = celsiusFahrenheit(celsius)
    print(f"{celsius} Celsius equivale a {resultado:.2f} Fahrenheit.")

elif escolha == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = fahrenheitFelsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit equivale a {resultado:.2f} Celsius.")

else:
    print("Escolha inválida.")
