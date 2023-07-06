import os
import csv

script_path = os.path.abspath(__file__)
directory = os.path.dirname(script_path)
#csv_file = 
csv_file=os.path.join(#'c','Users','Pined','ClassRepo',
                      #'UTA-VIRT-DATA-PT-06-2023-U-LOLC',
                      #'02-Homework','03-Python','Starter_Code',
                      #'PyBank',
                      directory,'Resources','budget_data.csv')

def calculate_total_fromcsv(file_path):
    total = 0
    with open(file_path,'rt') as file:
        csv_reader = csv.reader(file, delimiter=',')

        for row in csv_reader:
            record = float(row[0])
            total += record
    return total

result = calculate_total_fromcsv(csv_file)
print("Total:", result)