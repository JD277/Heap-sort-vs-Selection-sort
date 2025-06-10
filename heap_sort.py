import numpy
import time
import csv
import os
from datetime import datetime
from Algorithm import Algorithm 
class HeapSort(Algorithm):
    """
        A class to sort arrays using the Heap (max-Heap) method
    """
    def __init__(self):
        self.calls = 0

    def heapify(self, n, i):
        """
            **Description:**
                A fuction that heapfy an array to be sorted by the Heap method

            **Args:**
                n = Lenght of the array
                i = index of the array
        """
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.arr[i] < self.arr[l]:
            largest = l

        if r < n and self.arr[largest] < self.arr[r]:
            largest = r

        if largest != i:
            self.calls += 1
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def heap_sort(self):
        """
            **Description:**
                A function that sorts an array using the Heap method
        """
        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(i, 0)

    def sort(self, arr: str | list, id):
        """
            **Description:**
                A function that sorts an array using the Heap method

            **Args:**
                arr = The array that you will sort
        """
        if isinstance(arr, str):
            if not self.load_array_from_file(arr):
                print("Error loading array from file")
                return None
        else:
            self.arr = arr
        begining= time.perf_counter()
        self.heap_sort()
        end = time.perf_counter()
        data = {
            "prueba_id": id,
            "tamano_arreglo": len(self.arr),
            "tiempo_segundos": round(end - begining, 6),
            "llamadas_heapify": self.calls,
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.save_result_csv(result=data,file_name="resultados_heap_sort.csv")
        print(f"[Prueba {id}] Tiempo: {end - begining:.4f} segundos | Llamadas a heapify: {self.calls}")
        return self.arr

# Example usage
if __name__ == "__main__":
    heap_sort = HeapSort()
    arr = numpy.load("datos/Arreglo_1.npy").tolist()
    heap_sort.sort(arr, 1)   