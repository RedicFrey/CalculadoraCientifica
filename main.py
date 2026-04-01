import funcao_calculadora as fq

x = fq.calculadora()
print(x)

while True:
    a = input("deseja fazer mais alguma coisa ?\n1. sim\n2. nao\n").lower().strip()
    if a == "1" or a == "sim":
        x = fq.calculadora()
        print(x)
    else:
        print("Saindo...")
        break
