from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Acceder a las variables de entorno
aburrido = os.getenv('ABURRIDO')

# Imprimir variable de entorno
print(aburrido.capitalize())
print(type(aburrido))
