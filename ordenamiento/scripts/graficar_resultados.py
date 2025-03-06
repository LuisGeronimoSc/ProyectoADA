import os
import pandas as pd
import matplotlib.pyplot as plt

def graficar_resultados():
    resultados_path = "../data/resultados/tiempos.csv"

    if not os.path.exists(resultados_path):
        print("❌ No se encontró el archivo de resultados.")
        return

    # Leer el CSV (adaptado si usas separador ';')
    resultados = pd.read_csv(resultados_path, sep=';')

    # Verificamos las columnas que tiene para evitar errores
    print("\n✅ Datos cargados:")
    print(resultados.head())

    plt.figure(figsize=(10, 6))

    algoritmos = resultados['Algoritmo'].unique()

    for algoritmo in algoritmos:
        datos_algoritmo = resultados[resultados['Algoritmo'] == algoritmo]
        plt.plot(
            datos_algoritmo['Tamaño'],
            datos_algoritmo['Tiempo (segundos)'],
            marker='o',
            label=algoritmo
        )

    plt.title('Comparación de Algoritmos de Ordenamiento')
    plt.xlabel('Tamaño del dataset')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True)

    # Guardar la gráfica
    grafica_path = "../data/resultados/grafica_tiempos.png"
    plt.savefig(grafica_path)
    plt.show()

    print(f"\n✅ Gráfica guardada como {grafica_path}")

if __name__ == "__main__":
    graficar_resultados()