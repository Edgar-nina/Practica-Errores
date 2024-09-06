import math

# Definimos la función original h(x)
def h(x):
    return math.log(x)

# Definimos las derivadas de la función h(x) = ln(x)
def h_primera(x):
    return 1/x

def h_segunda(x):
    return -1/(x**2)

def h_tercera(x):
    return 2/(x**3)

def h_cuarta(x):
    return -6/(x**4)

# Expansión de Taylor hasta cuarto orden alrededor de punto_base
def taylor_expansion_ln(punto_base, punto_aprox, orden):
    aproximacion = h(punto_base)
    if orden >= 1:
        aproximacion += h_primera(punto_base) * (punto_aprox - punto_base)
    if orden >= 2:
        aproximacion += (h_segunda(punto_base) * (punto_aprox - punto_base)**2) / math.factorial(2)
    if orden >= 3:
        aproximacion += (h_tercera(punto_base) * (punto_aprox - punto_base)**3) / math.factorial(3)
    if orden >= 4:
        aproximacion += (h_cuarta(punto_base) * (punto_aprox - punto_base)**4) / math.factorial(4)
    return aproximacion

# Cálculo del error relativo porcentual verdadero
def error_relativo_porcentual_ln(valor_real, valor_aproximado):
    return abs((valor_real - valor_aproximado) / valor_real) * 100

# Parámetros
punto_base = 1    # Punto base
punto_aprox = 2.5 # Valor donde queremos aproximar
valor_real = h(punto_aprox)  # Valor verdadero de ln(2.5)

# Calcular aproximaciones y errores
for orden in range(5):
    valor_aproximado = taylor_expansion_ln(punto_base, punto_aprox, orden)
    error = error_relativo_porcentual_ln(valor_real, valor_aproximado)
    print(f"Aproximación de orden {orden}: {valor_aproximado}")
    print(f"Error relativo porcentual: {error:.5f}%\n")
