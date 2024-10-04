# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicita ao usuário o peso e a altura
peso = float(input("Digite seu peso em kg: "))89
altura = float(input("Digite sua altura em metros: "))1.74

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
