import numpy as np
import pandas as pd
import os

# Definir las variables conocidas
ancho_canal = 20  # Ancho del canal en metros
profundidad_canal = 0.3  # Profundidad del canal en metros
rugosidad = 0.03  # Coeficiente de rugosidad
pendiente = 0.0003  # Pendiente

# Definir los rangos de incertidumbre para rugosidad y pendiente
rugosidad_rango = (0.027, 0.033)
pendiente_rango = (0.00027, 0.00033)

# Incrementos para diferencias finitas
delta_rugosidad = 0.001  # Incremento pequeño para rugosidad
delta_pendiente = 0.00001  # Incremento pequeño para pendiente

# Definir la fórmula de Manning para el flujo en un canal rectangular
def flujo_manning(ancho, profundidad, rugosidad, pendiente):
    return (1 / rugosidad) * ((ancho * profundidad)**(5/3)) / ((ancho + 2 * profundidad)**(2/3)) * np.sqrt(pendiente)

# Calcular el flujo nominal
flujo_nominal = flujo_manning(ancho_canal, profundidad_canal, rugosidad, pendiente)

# Análisis de sensibilidad de primer orden (diferencias finitas)
# Sensibilidad con respecto a la rugosidad
flujo_rugosidad_mas = flujo_manning(ancho_canal, profundidad_canal, rugosidad + delta_rugosidad, pendiente)  # Flujo con rugosidad + delta_rugosidad
flujo_rugosidad_menos = flujo_manning(ancho_canal, profundidad_canal, rugosidad - delta_rugosidad, pendiente)  # Flujo con rugosidad - delta_rugosidad
derivada_rugosidad = (flujo_rugosidad_mas - flujo_rugosidad_menos) / (2 * delta_rugosidad)  # Derivada numérica central
incertidumbre_rugosidad = (rugosidad_rango[1] - rugosidad_rango[0]) / 2  # Incertidumbre en rugosidad
sensibilidad_rugosidad = abs(derivada_rugosidad * incertidumbre_rugosidad)

# Sensibilidad con respecto a la pendiente
flujo_pendiente_mas = flujo_manning(ancho_canal, profundidad_canal, rugosidad, pendiente + delta_pendiente)  # Flujo con pendiente + delta_pendiente
flujo_pendiente_menos = flujo_manning(ancho_canal, profundidad_canal, rugosidad, pendiente - delta_pendiente)  # Flujo con pendiente - delta_pendiente
derivada_pendiente = (flujo_pendiente_mas - flujo_pendiente_menos) / (2 * delta_pendiente)  # Derivada numérica central
incertidumbre_pendiente = (pendiente_rango[1] - pendiente_rango[0]) / 2  # Incertidumbre en pendiente
sensibilidad_pendiente = abs(derivada_pendiente * incertidumbre_pendiente)

# Crear un DataFrame para los resultados
resultados = {
    'Variable': ['Rugosidad (n)', 'Pendiente (S)'],
    'Flujo Nominal (Q) [m^3/s]': [flujo_nominal, flujo_nominal],
    'Derivada Numérica (dQ/dVariable)': [derivada_rugosidad, derivada_pendiente],
    'Incertidumbre': [incertidumbre_rugosidad, incertidumbre_pendiente],
    'Sensibilidad (dQ/dVariable * Incertidumbre) [m^3/s]': [sensibilidad_rugosidad, sensibilidad_pendiente]
}

df_resultados = pd.DataFrame(resultados)

# Guardar el DataFrame en un archivo Excel
nombre_archivo = 'Resultados_Sensibilidad_Manning.xlsx'
ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)  # Ruta en el directorio actual

try:
    df_resultados.to_excel(ruta_archivo, index=False)
    print(f"Archivo de resultados guardado en: {ruta_archivo}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")

# Mostrar los resultados en consola
print(df_resultados)
