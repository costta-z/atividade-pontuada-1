import os
os.system("cls")

renda = float(input("Digite sua renda mensal: R$ "))
emprestimo = float(input("Digite o valor do empréstimo solicitado: R$ "))
prestacoes = int(input("Digite o número de prestações desejado: "))

valor_prestacao = emprestimo / prestacoes

if emprestimo <= 10 * renda and valor_prestacao <= 0.3 * renda:
    print("\nEmpréstimo pode ser concedido.")
else:
    print("\nEmpréstimo não pode ser concedido.")
