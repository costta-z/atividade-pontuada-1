import os
os.system("cls")


cor = input("Digite a cor do CD (Verde, Azul, Amarelo, Vermelho): ").strip().capitalize()
precos = {
    "Verde": 10.00,
    "Azul": 20.00,
    "Amarelo": 30.00,
    "Vermelho": 40.00
}
if cor in precos:
    print(f"O preço do CD {cor} é R$ {precos[cor]:.2f}")
else:
    print("Cor inválida. Por favor, digite uma das cores: Verde, Azul, Amarelo ou Vermelho.")
