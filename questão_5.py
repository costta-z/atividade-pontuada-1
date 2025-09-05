import os
os.system("cls")

def calculadora():
    
  
    operacao = input("Digite o código da operação (+, -, *, ou /): ")

    
    try:
        num1 = int(input("Digite o primeiro valor inteiro {A}: "))
        num2 = int(input("Digite o segundo valor inteiro {B}: "))
    except ValueError:
        print("Erro: Por favor, insira valores inteiros válidos.")
        return

    
    if operacao == '+':
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} é: {resultado}")
    elif operacao == '-':
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} é: {resultado}")
    elif operacao == '*':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} é: {resultado}")
    elif operacao == '/':
        
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Erro: Operação inválida. Use +, -, * ou /.")


calculadora()