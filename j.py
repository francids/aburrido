nombres = ["juan", "pedro", "maria", "jose", "luis"]
apellidos = ["perez", "gomez", "gonzales", "rodriguez", "sanchez"]

personas = [nombre.capitalize() + " " + apellido.capitalize() for nombre, apellido in zip(nombres, apellidos)]

print(personas)

# ...

numbers = list(range(1, 100))

impares = [i for i in numbers if i % 2 != 0]
pares = [p for p in numbers if p % 2 == 0]

print(impares)
print(pares)
