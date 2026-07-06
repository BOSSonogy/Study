import csv
import json
import xml.etree.ElementTree
import logging
from pathlib import Path

#Task 1

BASE_DIR = Path(__file__).parents[1]
CSV_DIR = BASE_DIR / "ideas_for_test" / "work_with_csv"
OUTPUT_DIR = Path(__file__).parent

file1 = CSV_DIR / "random.csv"
file2 = CSV_DIR / "rmc.csv"
result = OUTPUT_DIR / "result_Dobranskyi.csv"

unique_rows = set()

for file in (file1, file2):
    with open(file, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            unique_rows.add(tuple(row))

with open(result, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(sorted(unique_rows))

print(f"Saved at: {result}")


#Task 2

JSON_DIR = BASE_DIR / "ideas_for_test" / "work_with_json"
LOG_FILE = Path(__file__).parent / "json_Dobranskyi.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

for json_file in JSON_DIR.glob("*.json"):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"{json_file.name} is invalid JSON. {e}")

print("Done.")
print(f"Log_file: {LOG_FILE}")


#Task 3

XML_FILE = BASE_DIR / "ideas_for_test" / "work_with_xml" / "groups.xml"

logger = logging.getLogger("xml_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(console)


def find_incoming(group_number):
    tree = xml.etree.ElementTree.parse(XML_FILE)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == str(group_number):
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                return incoming.text

            return "timingExbytes/incoming not found"

    return "Group not found"


logger.info(find_incoming(2))