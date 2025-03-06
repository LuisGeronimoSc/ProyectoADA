import os
import time
import pandas as pd
import numpy as np
from algoritmos import bubble_sort, insertion_sort, merge_sort, quick_sort

def generar_dataset(tamano):
    return np.random.randint(0, 10000, size=tamano).tolist()

def ejecutar_experimento():
    tamanos = [100, 500, 1000, 5000]
    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    resultados = []

    # Crear carpetas si no existen
    os.makedirs("../data/datasets", exist_ok=True)
    os.makedirs("../data/resultados", exist_ok=True)

    for tam in tamanos:
        datos = generar_dataset(tam)
        dataset_path = f"../data/datasets/dataset_{tam}.csv"
        pd.DataFrame({"Valor": datos}).to_csv(dataset_path, index=False)

        for nombre, algoritmo in algoritmos.items():
            datos_copia = datos.copy()
            inicio = time.time()
            algoritmo(datos_copia)
            fin = time.time()
            tiempo = fin - inicio
            resultados.append({
                "Algoritmo": nombre,
                "Tamaño": tam,
                "Tiempo (segundos)": tiempo
            })
            print(f"{nombre} con {tam} elementos tomó {tiempo:.4f} segundos")

    resultados_df = pd.DataFrame(resultados)

    # Guardar resultados ordenados
    resultados_df = resultados_df.sort_values(by=["Tamaño", "Algoritmo"])

    # Guardar CSV con separador ;
    resultados_df.to_csv("../data/resultados/tiempos.csv", sep=';', index=False, encoding='utf-8')

    # Guardar también en Excel
    resultados_df.to_excel("../data/resultados/tiempos.xlsx", index=False)

    print("\n✅ Experimentos finalizados y resultados guardados correctamente en CSV y Excel.")

if __name__ == "__main__":
    ejecutar_experimento()
