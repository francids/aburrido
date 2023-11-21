decimal_a_binario = lambda n: bin(n)[2:]
binario_a_decimal = lambda b: int(b, 2)

op = input("¿Quieres convertir de decimal a binario (dab) o de binario a decimal (bad)? ")
numero = input("Ingresa el número que quieres convertir: ")

if op.lower() == 'dab':
    resultado = decimal_a_binario(int(numero))
elif op.lower() == 'bad':
    resultado = binario_a_decimal(numero)
else:
    resultado = "Opción no válida."

print("El resultado de la conversión es:", resultado)
