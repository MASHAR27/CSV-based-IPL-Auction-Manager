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
            
     
      
        
def update_cricketer():
    """Finds an existing cricketer record and then modifies their info and then rewrites the new updated info  """
    upd_name = input("Please enter the cricketer's name who's record you want to update: ").strip().lower()
    if upd_name == "":
        print("Name can't be empty")
        return None
    try :
      # first I want to store the original records in a variable to update and write to later
      found = False
      with open(ipl_path,"r") as file:
          storer = csv.reader(file)
          orignal_record = list(storer)
      for record in orignal_record:
          if record and record[0].lower().strip() == upd_name:
              found = True
              print("Choose the value that you want to replace ")
              print("Enter 0 for changing the cricketer's name")
              print("Enter 1 for updating the cricketer's age")
              print("Enter 2 for updating the cricketer's  IPL team")
              print("Enter 3 for updating the cricketer's number of IPL matches")
              print("Enter 4 for updating the cricketer's  international team")
              print("Enter 5 for updating whether the cricketer has played international cricketer or not")
              print("Enter 6 for updating the cricketer's Auction price")
              option = input("Please choose from the above to update the fields: ").strip()
              if option == "":
                  print("Option can't be empty")
                  return None
              match option:
                  case "0":
                      new_name = input(f"Please enter the new name of {record[0]} ").strip()
                      if new_name == "":
                          print("New name can't be empty")
                          return None
                      record[0] = new_name
                      with open(ipl_path,"w") as file:
                          new_writer = csv.writer(file)
                          new_writer.writerows(orignal_record)
                      print("Successfully updated the new name for the cricketer!")
                  case "1":
                      new_age = input("Please enter the new age: ").strip()
                      if new_age == "":
                          print("New age can't be empty")
                          return None
                      if  not new_age.isdigit():
                          print("The new age must be a numeric value")
                          return None
                      if int(new_age) <=0:
                          print("New Age must be at least greater than 0")
                          return None
                      record[1] =  new_age
                      with open(ipl_path,"w") as file:
                          writer = csv.writer(file)
                          writer.writerows(orignal_record)
                      print("Successfully updated the cricketer's age") 
                  case "2":
                      new_ipl = input("Please enter the abbrieviation of the new IPl team you want for this player: ").strip()
                      if new_ipl == "":
                          print("New IPL team can't be empty")
                          return None
                      record[2] = new_ipl
                      with open(ipl_path,"w") as file:
                          writer = csv.writer(file)
                          writer.writerows(orignal_record)
                      print("Successfully updated the new IPL team for the cricketer!")    
                  case "3":
                      new_matches = input("Enter the new number of IPL matches:  ").strip()
                      if new_matches == "":
                           print("The number of matches can't be empty")
                           return None
                      if  not new_matches.isdigit():
                          print("The number of matches must be a numeric value")
                          return None
                      if int(new_matches) <0:
                          print("New number of matches must be zero or a positive number")
                          return None
                      record[3] = new_matches
                      with open(ipl_path,"w") as file:
                           writer = csv.writer(file)
                           writer.writerows(orignal_record)
                      print("Successfully updated the number of IPL matches for the cricketer!")  
                  case "4":
                      new_intl_team = input("Enter the new international team:  ").strip()
                      if new_intl_team == "":
                           print("New International team can't be empty")
                           return None
                      record[4] = new_intl_team
                      with open(ipl_path,"w") as file:
                          writer = csv.writer(file)
                          writer.writerows(orignal_record)
                      print("Successfully updated the new International team for the cricketer!")       
                  case "5":
                      played_intl = input("Enter the new True or False for whether the cricketer has played international cricket or not:  ").strip()
                      if played_intl == "":
                          print("It can't be empty , please enter True or False")
                          return None
                      if played_intl != "True" and played_intl != "False":   
                          print("Please enter True or False only") 
                          return None    
                      record[5] = played_intl
                      with open(ipl_path,"w") as file: 
                          writer = csv.writer(file)    
                          writer.writerows(orignal_record)                
                      print("Successfully updated whether the cricketer has played International cricket or not!")                             
                  case "6":
                      auc_price = input("Enter the new auction price:  ").strip() 
                      if auc_price == "":
                          print("New Auction price can't be empty")   
                          return None                         
                      if not auc_price.isdigit():
                         print("The new auction price must be a numeric value")  
                         return None
                      if int(auc_price) <=0:  
                        print("New auction price must be at least greater than 0")    
                        return None                 
                      record[6] =  auc_price 
                      with open(ipl_path,"w") as file:
                           writer = csv.writer(file)
                           writer.writerows(orignal_record) 
                      print("Successfully updated the cricketer's auction price")                                                
                  case _:
                      print("Please only enter from the available options")
                      
      if not found:
          print(f"Couldn't find {upd_name}")
          return None      
    except FileNotFoundError:
        print("Couldn't find the file which contained IPL auction records and info")
        return None 
                                                    
                                                
                                           
                                                
                                               
                                           
                                               
                                               
                                           
                                            
                                            
                                
                                               
                                               
                                              
                                       
                      
                       
                                               
                                                
                        
                                               
                                                
                                            
                      
                                               
                                                
                                           
                                                
                                                
                                         
                                                
                                                
                          
                                                    
                                    
                          
                          
                              
              
