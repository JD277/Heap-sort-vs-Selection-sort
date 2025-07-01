# Comparación de Algoritmos de Ordenamiento – Heap Sort vs Selection Sort

Este proyecto compara el rendimiento de dos algoritmos clásicos de ordenamiento:

- **Heap Sort** (muy eficiente, O(n log n))
- **Selection Sort** (simple pero ineficiente, O(n²))

El objetivo es evaluar su desempeño en términos de **tiempo de ejecución** y **número de operaciones realizadas** sobre arreglos de gran tamaño generados con `numpy`.
vide explicativo: https://drive.google.com/file/d/1dB48E92MYSEp2lgxDg-WYta5YSBhR4qN/view?usp=sharing

---

## 📁 Estructura del Proyecto

```
proyecto_ordenamiento/
│
├── heap_sort.py                  # Implementación del Heap Sort
├── selection_sort.py             # Implementación del Selection Sort (versión nativa)
├── selection_sort_numpy.py       # Implementación del Selection Sort usando NumPy
├── Algorithm.py                  # Clase base compartida por ambos algoritmos
├── resultados/                   # Carpeta con archivos CSV de resultados
│   ├── resultados_heap_sort.csv
│   ├── resultados_selection_sort_normal.csv
│   └── resultados_selection_sort_numpy.csv
├── datos/                        # Carpeta con arreglos .npy de prueba
│   ├── Arreglo_1.npy
│   ├── Arreglo_2.npy
│   └── ...
├── data_analysis.ipynb           # Análisis de datos con gráficos usando pandas y matplotlib
└── README.md                     # Este archivo
```

---

## 📌 Descripción de los Archivos

| Archivo | Descripción |
|--------|-------------|
| `heap_sort.py` | Implementación del algoritmo **Heap Sort** heredado de la clase base `Algorithm`. Mide tiempo de ejecución y llamadas a `heapify`. |
| `selection_sort.py` | Implementación estándar del algoritmo **Selection Sort** con medición de comparaciones e intercambios. |
| `selection_sort_numpy.py` | Versión optimizada del **Selection Sort** usando `numpy` para mejorar el rendimiento. |
| `Algorithm.py` | Clase base que provee funcionalidad común: carga de arreglos desde archivos `.npy` y guardado de resultados en CSV. |
| `resultados/*.csv` | Resultados obtenidos tras múltiples ejecuciones de cada algoritmo. Incluye tiempo de ejecución y operaciones realizadas. |
| `datos/*.npy` | Archivos de datos pregenerados con `numpy` usados para las pruebas. |
| `data_analysis.ipynb` | Cuaderno de Jupyter con el análisis detallado de los resultados, incluyendo gráficos comparativos. |

---

## 📊 Objetivo del Proyecto

Comparar empíricamente el rendimiento de los siguientes algoritmos:

| Algoritmo | Complejidad Temporal | Características |
|-----------|----------------------|-----------------|
| **Heap Sort** | O(n log n) | Eficiente para grandes volúmenes de datos |
| **Selection Sort (Normal)** | O(n²) | Simple pero muy lento para conjuntos grandes |
| **Selection Sort (NumPy)** | O(n²) | Mejora leve en tiempo gracias a `numpy`, pero complejidad igual |

---

## 🔍 Metodología

- Se utilizaron arreglos de tamaños fijos (desde 20,000 hasta 200,000 elementos).
- Cada algoritmo se ejecutó múltiples veces para obtener promedios estadísticamente representativos.
- Se midieron:
  - Tiempo de ejecución (`time.perf_counter`)
  - Número de comparaciones o llamadas realizadas
  - Tamaño del arreglo procesado
- Los resultados se guardaron en archivos `.csv` y se analizaron posteriormente con `pandas` y `matplotlib`.

---

## 📈 Resultados Principales

### ⏱️ Tiempo Promedio de Ejecución

| Algoritmo | Tamaño del Arreglo | Tiempo Promedio |
|----------|--------------------|------------------|
| Heap Sort | 200,000 | ~2.45 segundos |
| Selection Sort (Python) | 20,000 | ~42 segundos |
| Selection Sort (NumPy) | 20,000 | ~30 segundos |

> **Observación:** Aunque `Selection Sort` con `numpy` mejora ligeramente, sigue siendo **mucho más lento** que `Heap Sort`.

---

### 📉 Número de Operaciones

| Algoritmo | Operaciones Promedio |
|----------|----------------------|
| Heap Sort | ~3,150,000 llamadas |
| Selection Sort | ~199,990,000 comparaciones |

> Heap Sort realiza menos del **0.1%** de las operaciones que hace Selection Sort.

---

## 📁 Requisitos del Proyecto

Para ejecutar este proyecto necesitas tener instalado lo siguiente:

- Python 3.x
- Librerías:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn` (opcional)

Puedes instalarlas con:

```bash
pip install numpy pandas matplotlib seaborn
```

---

## 🛠️ Uso del Proyecto

1. **Genera los arreglos de prueba** (si aún no están):
   ```python
   import numpy as np
   arr = np.random.randint(0, 1_000_000, size=200000)
   np.save("datos/Arreglo_1.npy", arr)
   ```

2. **Ejecuta los algoritmos**
   ```python
   from heap_sort import HeapSort
   from selection_sort import SelectionSort

   hs = HeapSort()
   hs.sort("datos/Arreglo_1.npy", id=1)
   ```

3. **Analiza los resultados con `pandas`**
   - Abre `data_analysis.ipynb` en Jupyter Notebook
   - Carga los archivos CSV
   - Genera gráficos comparativos

---

## 📚 Recursos Adicionales

- [Documentación oficial de NumPy](https://numpy.org/doc/)
- [Documentación de Pandas](https://pandas.pydata.org/pandas-docs/stable/)
- [Guía rápida de matplotlib](https://matplotlib.org/stable/contents.html)

---

## ✅ Conclusión

Este proyecto demuestra cómo la elección del algoritmo afecta significativamente el rendimiento real, incluso en el mismo lenguaje (Python). **Heap Sort** destaca como una opción altamente escalable, mientras que **Selection Sort**, aunque útil para enseñanza, debe evitarse en entornos reales debido a su alta complejidad temporal.

---

## 🤝 Autor

**Jesús Alcalá**  
C.I: 31.205.548  
Universidad de Oriente – Núcleo de Anzoátegui  
Taller de Análisis y Diseño de Algoritmos  
Sección: 01  
```

---
