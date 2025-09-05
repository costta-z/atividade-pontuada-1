
import os
from re import match
os.system("cls")

# DADOS

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2


print(f"A média do aluno é: {media:.2f}")


if media >= 6.0:
    print("Parabéns! O aluno está aprovado.")
elif 4.1 <= media <= 5.9:
    print("O aluno está em recuperação.")
else:
    print("O aluno foi reprovado.")



