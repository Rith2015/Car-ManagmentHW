# Car Management System

This project is a simple Python-based car management system that uses SQLite for storing data. The system allows you to add customers, manage their car information, search, update, delete, and display all records stored in the database.

## Features

- **Add Customer**: Add a new customer with their car information.
- **Add Car Info**: Add car information for an existing customer.
- **Edit Car Info**: Update the car details for a specific customer.
- **Delete Car**: Remove a car entry for a specific customer.
- **Show All Records**: Display all customer-car records in the database.
- **Search**: Search for a specific car by customer name, car color, and brand.
- **Exit**: Clear the screen and exit the application.

## Installation

1. Clone this repository to your local machine.
2. Make sure you have Python installed (preferably Python 3.x).
3. Install SQLite if it is not already installed (SQLite is typically bundled with Python).
4. Run the script using Python.

```bash
python car_management.py
## Usage
When you run the script, a menu will be displayed with different options.
Select the operation you want to perform by entering the corresponding number.
Follow the prompts to enter the required information.
The database (cars.db) will be automatically created and updated with your inputs.
Code Overview
Main Components
Database Connection:

The script connects to an SQLite database named cars.db.
It creates a table Cars with columns: Customer, Color, and Brand if it doesn't already exist.
Menu System:

The MENU Enum provides the options for the user.
The menu() function displays the menu and handles user input.
Functions:

AddCustomer(): Adds a new customer with their car information.
customer_exists(): Checks if a customer already exists in the database.
AddCarInfo(): Adds a car to an existing customer.
EditList(): Edits an existing car record.
search(): Searches for a car by customer name, color, and brand.
deleteCar(): Deletes a specific car from the database.
Show_All(): Displays all car records in the database.
Exit_screen(): Clears the screen and exits the application.
Example
Here is an example of how the system works:

Add a Customer:

Select "6 - Add_Customer" from the menu.
Enter the customer's name, car color, and brand.
The system will confirm that the new customer has been added.
Add a Car for an Existing Customer:

Select "1 - Add" from the menu.
Enter the customer's name, car color, and brand.
The system will confirm that the car has been added for the customer.
Edit Car Information:

Select "2 - Edit" from the menu.
Enter the customer's name, old car details, and new car details.
The system will confirm that the car details have been updated.
Delete a Car:

Select "3 - Delete" from the menu.
Enter the customer's name, car color, and brand.
The system will confirm that the car has been deleted.
Show All Records:

Select "4 - Show_All" from the menu.
All car records will be displayed.
Search for a Car:

Select "5 - Search" from the menu.
Enter the customer's name, car color, and brand.
The system will display the matching car records or indicate that no matches were found.
Exit the Application:

Select "7 - Exit" from the menu.
The screen will clear, and the application will exit.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software.

Contributions
Contributions are welcome! If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.