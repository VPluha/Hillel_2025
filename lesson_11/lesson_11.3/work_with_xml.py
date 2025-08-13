"""
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number
і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

import logging
import xml.etree.ElementTree as ET
from pathlib import Path

# Configuring the logger for console output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_incoming_by_group_number(xml_path: Path, group_number: str):
    """
    Шукає у groups.xml елемент group з заданим number
    і повертає значення timingExbytes/incoming
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")
        if number is not None and number.text == group_number:
            timing = group.find("timingExbytes")
            if timing is not None:
                incoming = timing.find("incoming")
                if incoming is not None:
                    return incoming.text
    return None

# Path to XML file
xml_file = Path("/Users/vasyl.pliukhin/PycharmProjects/PythonLearning/Hillel_2025/lesson_11/lesson_11.3/work_with_xml/groups.xml")

# Using the function
group_num = "101"  # example
incoming_value = find_incoming_by_group_number(xml_file, group_num)

if incoming_value is not None:
    logging.info(f"For group/number={group_num} value timingExbytes/incoming: {incoming_value}")
else:
    logging.info(f"Group with number={group_num} not found or missing incoming")
