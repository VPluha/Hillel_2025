"""
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
Результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""

import json
import logging
from pathlib import Path

# Folder with JSON files
folder = Path("/Users/vasyl.pliukhin/PycharmProjects/PythonLearning/Hillel_2025/lesson_11/lesson_11.2/work_with_json" )

# Log-file
log_file = folder / "json__Pliukhin.log"

# Logging settings
logging.basicConfig(
    filename=log_file,
    filemode='w',  # log file rewriting on each startup
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Checking each file in a folder
for file in folder.iterdir():
    if file.is_file() and file.suffix.lower() == ".json":
        try:
            with open(file, mode='r', encoding='utf-8') as f:
                json.load(f)  # try to read as JSON
        except json.JSONDecodeError as e:
            logging.error(f"File {file.name} is not valid JSON: {e}")
        except Exception as e:
            logging.error(f"Error reading {file.name}: {e}")

print(f"Verification complete. Results in {log_file}")
