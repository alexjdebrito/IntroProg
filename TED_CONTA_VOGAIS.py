def conta_vogais(frase):
    
    vogais = 'aeiouAEIOU'
    
    contador = 0
    
    for char in frase:
        if char in vogais:
            contador += 1
    
    return contador

texto = input('Digite uma frase: ')

resultado = conta_vogais(texto)
print(f'A frase contém {resultado} vogais.')