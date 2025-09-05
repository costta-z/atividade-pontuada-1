import os
os.system("cls")

print("=== TABELA DE PREÇOS ===")

print("""
FRUTA    |   ATÉ 5 KG         |   ACIMA DE 5 KG
===============================================      
MORANGO  |   R$ 2,5 POR KG    |   R$ 2,20 POR KG
MAÇÃ     |   R$ 1,80 POR KG   |   R$ 1,50 POR KG

""")

quantidade_morango = float(input("Digite a quantidade (em kg)de morangos: "))
quantidade_maca = float(input("Digite a quantidade (em kg) de maçãs: "))


if quantidade_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20
valor_morango = quantidade_morango * preco_morango


if quantidade_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50
valor_maca = quantidade_maca * preco_maca


valor_total_bruto = valor_morango + valor_maca


quantidade_total_frutas = quantidade_morango + quantidade_maca
if quantidade_total_frutas >= 10 or valor_total_bruto > 15.00:
    desconto = valor_total_bruto * 0.10
    valor_a_pagar = valor_total_bruto - desconto
else:
    valor_a_pagar = valor_total_bruto


print(f"O valor a ser pago pelo cliente é: R$ {valor_a_pagar:.2f}")



