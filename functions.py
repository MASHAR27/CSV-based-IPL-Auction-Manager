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
                    
            
def filter_by_team():
    """ Retrieves all the player's who match the team's abbrieviation that the user enters """
    team_name = input("Enter the IPL team's abbrieviation who's players you want to search for, etc: rcb,MI :  ").strip().lower()
    if team_name == "":
        print("Team name can't be empty")
        return None
    try:
        found_atl_player = False
        with open(ipl_path,"r") as file:
            team_searcher = csv.reader(file)
            next(team_searcher)
            for row in team_searcher:
                if team_name == row[2].lower():
                    found_atl_player = True
                    print(f"Name is {row[0]}")
                    print(f"Age is {row[1]}")
                    print(f"Total number of IPL matches played:  {row[3]}")
                    print(f"International Team is  {row[4]}")
                    print(f"Has played international cricket?  {row[5]}")
                    print(f"Auction price:  {row[6]}")
                    print()
            if found_atl_player:
                    print(f"These are all the player in {team_name}")
                    return None
            else:
                print(f"No players in {team_name}")
    except  FileNotFoundError:
        print("Couldn't find the file which contained IPL auction records and info")
        return None        
                            
                    
                    
                    
def add_cricketer():
    """Asks the user for a cricketers info one by one and then adds it to the csv file's records """ 
    print("Please enter the cricketer's field one by one that you want to add to the records")   
    cricketer = []       
    name = input("Enter the cricketer's name:  ").strip()
    if name == "":
        print("Name can't be empty")
        return None 
    cricketer.append(name)
    age = input("Enter the cricketer's age: ").strip()
    if not age.isdigit():
        print("Age should be a numeric whole value")
        return None
    if int(age) <= 0:
        print("Cricketer's age must be a valid age not negative or zero")
        return None
    cricketer.append(age)
    ipl_team = input("Enter the ipl team's abbrieviation").strip()
    if ipl_team == "":
            print("Team name can't be empty")
            return None 
    cricketer.append(ipl_team)
    ipl_matches = input("Enter the number of IPL matches they played: ")
    if ipl_matches == "":
        ipl_matches = "0"
    if not ipl_matches.isdigit():
        print("IPL matches must be numeric value")
        return None
    if int(ipl_matches)<0:
        print("IPL matches must be greater than or equal to 0")
        return None
    cricketer.append(ipl_matches)  
    intl_team = input("Enter their international team: ").strip()
    if intl_team == "":
        print("International Team can't be empty")
        return None
    cricketer.append(intl_team)
    int_debut = input("Have they played International cricket? Enter only True or False").strip()
    if int_debut == "":
        print("It can't be empty , please enter True or False")
        return None
    if int_debut != "True" and int_debut != "False":
        print("Please enter True or False only")
        return None
    cricketer.append(int_debut)
    auc_price = input("Please enter the auction price of the cricketer:  ").strip()
    if not auc_price.isdigit():
        print("Auction price must be a number")
        return None
    if int(auc_price)<=0:
        print("Auction price must be greater than zero atleast")
        return None
    cricketer.append(auc_price)
    with open(ipl_path,"a") as file:
            crick_adder = csv.writer(file)
            crick_adder.writerow(cricketer)
    print(f"Added {cricketer[0]} successfully to the csv file")          
            
     
      
        
