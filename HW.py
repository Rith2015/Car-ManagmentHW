import sqlite3
import os
from enum import Enum
con=sqlite3.connect("cars.db")
cur=con.cursor()
# create a table if there isnt one already
cur.execute("CREATE TABLE IF NOT EXISTS Cars(Customer,Color, Brand)")
class MENU(Enum):
    Add=1
    Edit=2
    Delete=3
    Show_All=4
    Search=5
    Add_Customer=6
    Exit=7

def menu():
    for item in MENU: print(f'{item.value}-{item.name}')
    return MENU(int(input("Your Selection-")))

# adds new customer to list
def AddCustomer(Customer,carColor,carBrand):
    cur.execute(f"INSERT INTO cars VALUES('{Customer}','{carColor}','{carBrand}') ")
    con.commit()
    print(f"New customer name is {Customer} and his new car is : {carColor} {carBrand}")  
     
# finds if a customer is in list or not       
def customer_exists(customer_name):
    cur.execute("SELECT * FROM Cars WHERE Customer = ?", (customer_name,))
    return cur.fetchone() is not None

# adds new cars if there a mathing customer name on the list
def AddCarInfo(Customer,carColor,carBrand):
    if customer_exists(Customer):
        cur.execute(f"INSERT INTO cars VALUES('{Customer}','{carColor}','{carBrand}') ")
        con.commit()
        print(f"Car Added for {Customer}: {carColor} {carBrand}")
    else:
        print(f"{Customer} not found")

# edit a car info on the list
def EditList(Customer, oldColor,oldBrand,newColor,newBrand):
    if customer_exists(Customer):
        cur.execute("UPDATE cars SET Color=?, Brand=? WHERE Color=? AND Brand=? ",
                    (newColor,newBrand,oldColor,oldBrand))
        con.commit()
        print(f"Car of {Customer} updated to: {newColor} {newBrand}")
    else:
        print(f"{Customer} not found")

# search for cars in list by customer name and car color and brand
def search(Customer,carColor,carBrand):
    cur.execute("SELECT * FROM cars WHERE Customer=? AND Color=? AND Brand=?", (Customer,carColor,carBrand))
    found=cur.fetchall()
    if found:
        for car in found:
            print(f"Found: {car}")
    else:
        print(f"No car found for {Customer} with Color: {carColor} and Brand: {carBrand}") 
# Deletes cars from list
def deleteCar(customer,carColor,carBrand):
    cur.execute("DELETE From cars WHERE Customer=? AND Color=? AND Brand=?",
                (customer,carColor,carBrand))
    con.commit()
    print(f"The {carColor} {carBrand} of {customer} has been deleted")
# Show all info on the list
def Show_All():
    res=cur.execute("SELECT * FROM cars")
    for i in res.fetchall():
        print(i) 
# Exit selection screen and clean terminal screen
def Exit_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()
if __name__=="__main__":
    while True:
        UserSelection=menu()
        if UserSelection==MENU.Add:AddCarInfo(
            input("Customer Name: "),
            input("Car Color: "),
            input("Car Brand: ")
        )
        if UserSelection==MENU.Edit:EditList(
            input("Customer Name: "),
            input("Old Car Color: "),
            input("Old Car Brand: "),
            input("New Car Color: "),
            input("New Car Brand: ")),exit()
        if UserSelection==MENU.Delete:deleteCar(
            input("Customer Name: "),
            input("Car Color: "),
            input("Car Brand: "))
        if UserSelection==MENU.Show_All:Show_All()
        if UserSelection==MENU.Search:search(
            input("Customer Name: "),
            input("Car Color: "),
            input("Car Brand: "))
        if UserSelection==MENU.Add_Customer:AddCustomer(
            input("New Customer Name: "),
            input("Car Color: "),
            input("Car Brand: ")
        )
        
        if UserSelection==MENU.Exit:Exit_screen()
