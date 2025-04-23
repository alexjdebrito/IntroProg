print("Indique o comprimento dos três lados do triângulo")
a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))

if a == b == c:
    print("É um triângulo equilátero (todos os lados iguais).")
elif a == b or a == c or b == c:
    print("É um triângulo isósceles (dois lados iguais).")
else:
    print("É um triângulo escaleno (todos os lados diferentes).")