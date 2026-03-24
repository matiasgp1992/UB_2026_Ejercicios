#Se resuelven los ejercicios en el siguiente script
import os


##################
#   EJERCICIO 1  #
##################
def calcular_area(base, altura):
    res = base * altura
    print(res)

    return res

##################
#   EJERCICIO 2  #
##################
try:
    conectar()
except Exception as e:
    print(f"Error al conectar: {e}")

##################
#   EJERCICIO 3  #
##################
def saludar(usuario):
    print(usuario)
    print('-------')

##################
#   EJERCICIO 4  #
##################
def suma(a: int, b: int) -> int:
    return a + b

##################
#   EJERCICIO 5  #
##################
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

##################
#   EJERCICIO 6  #
##################
x = 10 + 5 * 2 / (1 + 1)

##################
#   EJERCICIO 7  #
##################
def dia_semana(dia: int) -> str:
    dias = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles',
            4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}
    return dias.get(dia, 'Día inválido')

##################
#   EJERCICIO 8  #
##################
def procesar(user, passw, admin):
    if not user: return
    if not passw: return
    if not admin: return
    log()

##################
#   EJERCICIO 9  #
##################
def es_mayor(edad: int) -> bool:
    return edad >= 18

##################
#   EJERCICIO 10 #
##################
API_KEY = os.getenv('API_KEY')

##################
#   EJERCICIO 11 #
##################

# --> NO SE COMO RESOLVERLO <--

##################
#   EJERCICIO 12 #
##################
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'