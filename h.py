cantidad = int(input("Ingrese la cantidad de elementos: "))
lista = []

for i in range(cantidad):
    lista.append(input(f"Ingrese el elemento número {i + 1}: ").lower())

# Eliminar elementos repetidos
lista = list(set(lista))
cantidad = len(lista)
print("\nLa lista es: ", end="")
for elemento in lista:
    print(elemento.capitalize(), end=", " if elemento != lista[-1] else ".")

print(f"\nLa cantidad de elementos real es: {cantidad}")
