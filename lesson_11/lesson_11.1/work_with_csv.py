"""
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
   Результат запишіть у файл result_<your_second_name>.csv
"""
import csv
from pathlib import Path

# Provide the path to the folder with the files
folder = Path("/Users/vasyl.pliukhin/PycharmProjects/PythonLearning/Hillel_2025/lesson_11/lesson_11.1")
file1 = folder / "r-m-c.csv"
file2 = folder / "rmc.csv"
result_file = folder / "result_Pliukhin.csv"

rows = []
header = None
seen = set()  # to track already added lines

# Read and collect unique lines in order of appearance
for file in (file1, file2):
    with open(file, mode = 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        file_header = next(reader)
        if header is None:
            header = file_header
        for row in reader:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                rows.append(row_tuple)

# Write down the result
with open(result_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"File without duplicates {result_file}")

#Alternative version
# import pandas as pd
# from pathlib import Path
#
# # Paths to files
# folder = Path("/Users/vasyl.pliukhin/PycharmProjects/PythonLearning/Hillel_2025/lesson_11/lesson_11.1")
# file1 = folder / "r-m-c.csv"
# file2 = folder / "rmc.csv"
#
# # Reading files
# df1 = pd.read_csv(file1)
# df2 = pd.read_csv(file2)
#
# # Merge and remove duplicates
# df_combined = pd.concat([df1, df2]).drop_duplicates()
#
# # Record the result
# result_file = folder / "result_Pliukhin.csv"
# df_combined.to_csv(result_file, index=False)
#
# print(f"Результат збережено у {result_file}")
