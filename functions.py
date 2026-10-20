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
    
    
    
                

def filter_by_auction_price():
    """ Will ask user for a price and then display all the cricketer who have an auction price greater than or equal to that price   """
    price = input("Please enter a price for which you want to view all the cricketer having equal to or greater than that auction price: ").strip()
    if price == "":
            print("Price can't be empty")
            return None
    if not price.isdigit():
        print("The price must be a number!")
        return None
    
    price = int(price)    
    try:
        with  open(ipl_path,"r") as file:
            price_reader = csv.reader(file)
            found_atleast_one = False
            next(price_reader)
            for row in price_reader:
                if int(row[6]) >= price:
                    found_atleast_one = True
                    print(f"Name is {row[0]}")
                    print(f"Age is {row[1]}")
                    print(f"IPL team is {row[2]}")
                    print(f"Total number of IPL matches played:  {row[3]}")
                    print(f"International Team is  {row[4]}")
                    print(f"Has played international cricket?  {row[5]}")
                    print(f"Auction price:  {row[6]}")
                    
            if found_atleast_one:
                print("Those were all the cricketer's matching or greater than the price you entered")
                return None
            else:
                print("No cricketer's found having equal to greater than that price you entered")
                return None
                
                    
    except FileNotFoundError:
            print("Couldn't find the file which contained IPL auction records and info")
            return None               
                    
            
    