numero = int(input("Digite um número para ver a tabuada: "))

print ('--- FOR ---')
for n in range(1, 11):
    resultado = numero * n
    print(f"{numero} x {n} = {resultado}")

print ('--- WHILE ---')
ciclos = 1
while ciclos <=10:
    resultado = numero * ciclos
    print (f"{numero} x {ciclos} = {resultado}")
    ciclos += 1