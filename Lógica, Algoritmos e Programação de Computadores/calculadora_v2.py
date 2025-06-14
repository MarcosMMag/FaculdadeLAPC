# Calculadora em Python

# Colocando as formas de operação
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

# Operações usadas na calculadora
def calculadora(operacao, num1, num2):
    if operacao == "1":
        return somar(num1, num2)
    elif operacao == "2":
        return subtrair(num1, num2)
    elif operacao == "3":
        return multiplicar(num1, num2)
    elif operacao == "4":
        return dividir(num1, num2)
    else:
        return "Operação inválida."

# Loop do WHILE e input dos numeros e operação
saida = "s"
while saida.lower() != 'n':
    try:
        print("Operações: 1-Somar | 2-Subtrair | 3-Multiplicar | 4-Dividir")
        operacao = input("Escolha a operação (1/2/3/4): ")
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        resultado = calculadora(operacao, numero1, numero2)
        print("Resultado da operação:", resultado)
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

    saida = input("Deseja continuar? (S/N): ")