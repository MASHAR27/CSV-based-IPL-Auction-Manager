import csv
from pathlib import Path

records_path = Path(__file__).parent/"students.csv"
def read_records():
    """ Displays the current student records in the CSV file """
    try:
        with open(records_path, "r") as file:
            csv_read = csv.reader(file)
    except FileNotFoundError:
        print("Your csv student archive file couldn't be found")
    else:
                    
    
