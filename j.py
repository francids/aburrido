nombres = ["juan", "pedro", "maria", "jose", "luis"]
apellidos = ["perez", "gomez", "gonzales", "rodriguez", "sanchez"]

# nombresCap = list(map(lambda nombre: nombre.capitalize(), nombres))
# nombresCap2 = [nombre.capitalize() for nombre in nombres]

personas = list(map(lambda nombre, apellido: nombre.capitalize() + " " + apellido.capitalize(), nombres, apellidos))
personas2 = [nombre.capitalize() + " " + apellido.capitalize() for nombre, apellido in zip(nombres, apellidos)]

print(personas)
print(personas2)

# ...

numbers = list(range(1, 100))

impares = [i for i in numbers if i % 2 != 0]
pares = [p for p in numbers if p % 2 == 0]

print(impares)
print(pares)
