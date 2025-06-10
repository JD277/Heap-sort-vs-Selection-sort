import os 
import csv
import numpy

class Algorithm:

    def __init__(self):
        self.arr = None
    
    def save_result_csv(self,result:dict,file_name : str = "resultados.csv"):
        """
            Add new row to a csv file with critical data about the output

            **Args:**
                result = a dictionary with the data}
                file_name = The taret path to save the file
        """
        file_exists = os.path.isfile(file_name)
        with open(file_name, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=result.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(result)

    def load_array_from_file(self, file_name : str, non_numpy_list=True):
        """
            Load the array from the sample data

            **Args:**
                file_name = is the path of .npy to be loaded
        """
        try:
            if non_numpy_list:
                self.arr = numpy.load(file_name).tolist()
            else:
                self.arr = numpy.load(file_name)
            self.arr = numpy.load(file_name).tolist()
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return False
        except Exception as e:
            print(f"Error loading array from file: {e}")
            return False
        return True