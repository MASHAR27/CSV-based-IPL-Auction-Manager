import csv
from pathlib import Path
from functions import search_cricketer,filter_by_auction_price,filter_by_team,add_cricketer,update_cricketer,delete_cricketer,sort_cricketers

print("Welcome to IPL Cricketer Auction  Manager for CSV files! ")
record_path = Path(__file__).parent/"ipl.csv"
while True:
    print("Please choose amongst the options:  ")
    print("Enter 1 for searching for a cricketer by name and then if it exist's display his records ")
    print("Enter 2 for entering an auction price to display all the cricketer who have an auction price greater than or equal to that price")
    print("Enter 3 for printing all the cricketers belonging to a specific IPL team")
    print("Enter 4 for adding a new cricketer's record to the csv file")
    print("Enter 5 for updating an existing cricketer's record ")
    print("Enter 6 for deleting an existing cricketer's record")
    print("Enter 7 for printing the cricketer's record sorted by either age or IPL matches, or auction price")
    print("Enter 8 for Exiting the menu ")
    choice = input("Please enter from the above choices: ").strip()
    if choice not in ["1","2","3","4","5","6","7","8"]:
        print("Please enter a valid choice")
        continue
    match choice:
        case "1":
            search_cricketer()
        case "2":
            filter_by_auction_price()
        case "3":
            filter_by_team()
        case "4":
            add_cricketer()
        case "5":
            update_cricketer()
        case "6":
            delete_cricketer()
        case "7":
            sort_cricketers()
        case _:
            print("Thanks for using the application!")
            break

            
   
            
            
            
            
    
    