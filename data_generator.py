# datos_generados.py
import numpy as np
import os

def generar_y_guardar_arreglo(tamano=200_000, carpeta="datos", nombre_archivo="arreglo_200000.npy"):
    # Crear carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    ruta_completa = os.path.join(carpeta, nombre_archivo)

    print(f"Generando arreglo de {tamano} elementos...")
    arr = np.random.randint(0, 1_000_000, tamano)

    print(f"Guardando arreglo en '{ruta_completa}'...")
    np.save(ruta_completa, arr)
    print("Arreglo guardado exitosamente.")

if __name__ == "__main__":
    for i in range(1, 11):
        generar_y_guardar_arreglo(tamano=20000, nombre_archivo=f"Arreglo_{i}.npy", carpeta="datosSS")
