import csv
from pathlib import Path

ipl_path = Path(__file__).parent/"ipl.csv"

def search_cricketer():
    """ This functions asks the user for the cricketer's name then removes white-space and lowercaps for comparison with our records"""
    name_for_search = input("Please enter the cricketer's name you want to search for in the IPL Auction:  ").strip().lower()
    if name_for_search == "":
        print("Name can't be empty of the cricketer")
        return None
    try:
        with  open(ipl_path,"r") as file:
            name_reader = csv.reader(file)
            next(name_reader)
            for row in name_reader:
                if name_for_search in row[0].lower():
                    print(f"Found {name_for_search}! ")
                    print(f"Age is {row[1]}")
                    print(f"IPL team is {row[2]}")
                    print(f"Total number of IPL matches played:  {row[3]}")
                    print(f"International Team is  {row[4]}")
                    print(f"Has played international cricket?  {row[5]}")
                    print(f"Auction price:  {row[6]}")
                    return None
                
            print(f"Couldn't fine {name_for_search} in the records!")
            return None              
                    
    except FileNotFoundError:
        print("Couldn't find the file which contained IPL auction records and info")
        return None
    
    
    
                

