# Solicita o salário mensal do usuário
salario = float(input("Digite seu sálario, em reais, para cálculo do Imposto de Renda: "))

# Calcula o imposto com base nas faixas
if salario <= 2000:
    imposto = 0
elif salario <= 3500:
    imposto = salario * 0.10
else:
    imposto = salario * 0.15

# Exibe o valor do imposto
print(f"Imposto de renda a pagar: R$ {imposto:.2f}")