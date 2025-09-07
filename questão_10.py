import os
os.system("cls")

print("==== TABELA DE DESCONTOS ====")

print("""
CMBUSTIVEL |       QUANTIDADE     |  DESCONTO POR
           |        VENDIDA       |     LITRO
===========================================
ÁLCOOL     |ATÉ 25 LITROS         | 10%
ÁLCOOL     |ACIMA DE 25 LITROS    | 20%
GASOLINA   |TÉ 25 LITRO           | 15%
GASOOLINA  |ACIMA DE 25 LITROS    | 30%
      

""")

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").upper()

preco_alcool = 3.79
preco_gasolina = 6.59

if tipo == "A":
    preco = preco_alcool
    if litros <= 25:
        desconto = 0.10
    else:
        desconto = 0.20
elif tipo == "G":
    preco = preco_gasolina
    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30
else:
    print("Tipo de combustível inválido!")
    exit()

valor_bruto = litros * preco
valor_desconto = valor_bruto * desconto
valor_pago = valor_bruto - valor_desconto

print(f"\nValor a pagar: R$ {valor_pago:.2f}")


