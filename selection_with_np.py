import numpy as np
import time
from datetime import datetime
from Algorithm import Algorithm  

class SelectionSortNumpy(Algorithm):
    """
    A class to sort arrays using Selection Sort with NumPy for better performance
    """

    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.arr = np.array([])  

    def selection_sort(self):
        """
        Sorts the array using Selection Sort algorithm with NumPy
        """
        n = len(self.arr)

        for i in range(n):
            min_idx = i

            
            min_val = self.arr[i]
            for j in range(i + 1, n):
                if self.arr[j] < min_val:
                    min_val = self.arr[j]
                    min_idx = j
                self.comparisons += 1 

            if min_idx != i:
                self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
                self.swaps += 1  

    def sort(self, arr: str | np.ndarray, id_prueba):
        """
        Loads and sorts an array using Selection Sort with NumPy

        Args:
            arr: Path to .npy file or NumPy array
            id_prueba: Test ID for logging
        """
        if isinstance(arr, str):
            if not self.load_array_from_file(arr, False):  
                print("Error loading array from file")
                return None
        else:
            self.arr = np.array(arr, dtype=np.int64)  

        start = time.perf_counter()
        self.selection_sort()
        end = time.perf_counter()

        duration = round(end - start, 6)

        data = {
            "prueba_id": id_prueba,
            "tamano_arreglo": len(self.arr),
            "tiempo_segundos": duration,
            "comparaciones": self.comparisons,
            "intercambios": self.swaps,
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.save_result_csv(result=data, file_name="resultados_selection_sort_numpy.csv")

        print(f"[Prueba {id_prueba}] Tiempo: {duration:.4f} segundos | Comparaciones: {self.comparisons} | Intercambios: {self.swaps}")


        self.comparisons = 0
        self.swaps = 0

        return self.arr.copy()  
    
if __name__ == "__main__":
    selection_sort = SelectionSortNumpy()
    for i in range (3):
        for i in range(1, 11):
            selection_sort.sort(f"datosSS/Arreglo_{i}.npy", i)
