import csv
from pathlib import Path
from functions import read_records,write_records

print("Welcome to Student's Grade Manager for CSV files! ")
record_path = Path(__file__).parent/"students.csv"
while True:
    print("Please choose amongst the options:  ")
    print("Enter 1 for reading the current file's records  ")
    print("Enter 2 for adding a new record to the file  ")
    print("Enter 3 for exiting")
    print()
    option = input("Please enter your choice: ")
    match option:
        case "1":
            if record_path.exists():
                read_records()
               
            else:
                record_path.touch()
                print("The file is empty!")    
    
        case "2":
            print("Please enter each field one by one so your record can be added to the csv file")
            record = []
            name = input("Enter the student's name: ").strip()
            record.append(name)
            id = input("Enter the student's ID : ").strip()
            record.append(id)
            grade = input("Enter the student's grade : ").strip()
            record.append(grade)
            course = input("Enter the student's course : ").strip()
            record.append(course)
            write_records(record)
        
        case "3":
            print("Exiting")
            break    
            
            
            
            
    
    