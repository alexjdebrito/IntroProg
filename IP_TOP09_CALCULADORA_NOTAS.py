notas = []
nota = 0

print("Digite as notas do aluno (de 0 a 10). Digite -1 para encerrar.")

while nota != -1:
    try:
        nota = float(input("Nota: "))
        if nota == -1:
            break
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota fora do intervalo. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nTotal de notas inseridas: {len(notas)}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
else:
    print("\nNenhuma nota foi registrada.")