# Calculadora de IMC
 Projeto da aula de Python

### Passo 1: Definir a Função para Calcular o IMC
Primeiro, precisamos definir uma função que calcule o IMC. Uma função em Python é um bloco de código que só é executado quando chamado. Aqui está como você pode definir a função `calcular_imc`:

```python
# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
```

### Passo 2: Solicitar ao Usuário o Peso e a Altura
Agora, precisamos pedir ao usuário que insira seu peso e altura. Usamos a função `input` para isso e convertemos a entrada para um número de ponto flutuante(decimais) (float):

```python
# Solicita ao usuário o peso e a altura
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
```

### Passo 3: Calcular o IMC
Com o peso e a altura fornecidos pelo usuário, podemos calcular o IMC chamando a função `calcular_imc`:

```python
# Calcula o IMC
imc = calcular_imc(peso, altura)
```

### Passo 4: Exibir o Resultado
Vamos exibir o IMC calculado. Usamos `print` para mostrar o resultado na tela, formatando o número para duas casas decimais:

```python
# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")
```

### Passo 5: Classificar o IMC
Finalmente, vamos classificar o IMC em categorias como "Abaixo do peso", "Peso normal", "Sobrepeso" e "Obesidade":

```python
# Classificação do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
```

### Código Completo
Aqui está o código completo junto:

```python
# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicita ao usuário o peso e a altura
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

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
