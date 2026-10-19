import csv
from pathlib import Path

records_path = Path(__file__).parent/"students.csv"
def read_records():
    """ Displays the current student records in the CSV file """
    try:
        with open(records_path, "r") as file:
            csv_read = csv.reader(file)
            for row in csv_read:
                        print(row[0])
                        print(row[1])
                        print(row[2])
                        print(row[3])
                        print()
    except FileNotFoundError:
        print("Your csv student archive file couldn't be found")
        return None
    else:
        print()    
        print("That's all the student's")
        return None
    
    
def write_records(record_list):
    """Takes in a list of string which has 4 fields related to the student record """
    with open(records_path,"w") as file:
             csv_writer = csv.writer(file)
             csv_writer.writerow(record_list)
    print("Saved the student record in csv file!")
    return None
          
            
                

    
