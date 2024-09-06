import math

# Definimos la función original g(x)
def g(x):
    return 25*x**3 - 6*x**2 + 7*x - 88

# Definimos las derivadas de la función g(x)
def g_primera(x):
    return 75*x**2 - 12*x + 7

def g_segunda(x):
    return 150*x - 12

def g_tercera(x):
    return 150

# Expansión de Taylor hasta tercer orden alrededor de x_base
def taylor_expansion(x_base, x_eval, orden):
    aproximacion = g(x_base)
    if orden >= 1:
        aproximacion += g_primera(x_base) * (x_eval - x_base)
    if orden >= 2:
        aproximacion += (g_segunda(x_base) * (x_eval - x_base)**2) / math.factorial(2)
    if orden >= 3:
        aproximacion += (g_tercera(x_base) * (x_eval - x_base)**3) / math.factorial(3)
    return aproximacion

# Cálculo del error relativo porcentual
def error_relativo_porcentual(valor_real, valor_aproximado):
    return abs((valor_real - valor_aproximado) / valor_real) * 100

# Parámetros
punto_base = 1   # Punto base de la expansión
punto_evaluacion = 3  # Valor donde queremos hacer la aproximación
valor_real = g(punto_evaluacion)  # Valor verdadero de la función en x = 3

# Calcular aproximaciones y errores
for orden in range(4):
    valor_aproximado = taylor_expansion(punto_base, punto_evaluacion, orden)
    error = error_relativo_porcentual(valor_real, valor_aproximado)
    print(f"Aproximación de orden {orden}: {valor_aproximado}")
    print(f"Error relativo porcentual: {error:.5f}%\n")
