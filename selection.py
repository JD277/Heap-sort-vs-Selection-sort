import time
from datetime import datetime
from Algorithm import Algorithm  # Clase base compartida

class SelectionSort(Algorithm):
    """
    A class to sort arrays using the Selection Sort method
    """

    def __init__(self):
        self.comparisons = 0  
        self.swaps = 0        

    def selection_sort(self):
        """
        Sorts the array using the Selection Sort algorithm
        """
        n = len(self.arr)

        for i in range(n):
            min_idx = i  

           
            for j in range(i + 1, n):
                self.comparisons += 1  
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j

            
            if min_idx != i:
                self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
                self.swaps += 1  

    def sort(self, arr: str | list, id_prueba):
        """
        Sorts an array and logs performance data

        Args:
            arr: Path to .npy file or list of numbers
            id_prueba: Test ID for logging
        """
        if isinstance(arr, str):
            if not self.load_array_from_file(arr):  # Método heredado
                print("Error loading array from file")
                return None
        else:
            self.arr = arr 

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

        self.save_result_csv(result=data, file_name="resultados_selection_sort_normal.csv")

        print(f"[Prueba {id_prueba}] Tiempo: {duration:.4f} segundos | Comparaciones: {self.comparisons} | Intercambios: {self.swaps}")

        
        self.comparisons = 0
        self.swaps = 0

        return self.arr
    
if __name__ == "__main__":
    selection_sort = SelectionSort()

    for i in range(1, 11):
        selection_sort.sort(f"datosSS/Arreglo_{i}.npy", i) 