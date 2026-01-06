# MainSystem Class, Controls overall program flow and user interaction

from vehicle import Vehicle
from customer import Customer
from rental import Rental
from payment import Payment
from file_manager import FileManager
from datetime import datetime
import os


class MainSystem:
    def __init__(self):
        self.currentUser = None
        self.vehicle_file = FileManager("vehicles.txt")
        self.customer_file = FileManager("customers.txt")
        self.rental_file = FileManager("rentals.txt")
        self.payment_file = FileManager("payments.txt")
        self.user_file = FileManager("users.txt")

# Initialize files with headers if they are empty
        self._initialize_file_headers()

    def _initialize_file_headers(self):
# Add column headers to file to make it readable when opened in the text editor

        files_and_headers = {
            "vehicles.txt": "VehicleID|Type|Brand|RentalRate|Status",
            "customers.txt": "CustomerID|Name|ContactDetails|LicenseNumber",
            "rentals.txt": "RentalID|CustomerID|VehicleID|RentalDate|ReturnDate|TotalCost",
            "payments.txt": "PaymentID|RentalID|AmountPaid|PaymentDate",
            "users.txt": "Username|Password"
        }

        for filename, header in files_and_headers.items():
# Only add header if file is empty
            if os.path.exists(filename) and os.path.getsize(filename) == 0:
                with open(filename, 'w') as f:
                    f.write(header + '\n')

    def clear_screen(self):
# Clears the console screen to keep the output clean
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
# Waits for user to press Enter before continuing
        input("\nPress Enter to continue...")


# AUTHENTICATION SYSTEM

    def signup(self):
# Registers a new user in the system
        self.clear_screen()
        print("\n" + "*" * 60)
        print("SIGNUP - CREATE NEW ACCOUNT")
        print("*" * 60)

        try:
# Get username
            username = input("Enter username: ").strip()
            if not username:
                print("Error: Username cannot be empty")
                self.pause()
                return False

# Check if username already exists
            existing_users = self.user_file.read_from_file()
            for user_line in existing_users:
                if user_line.startswith("Username|"):  # Skip header
                    continue
                stored_username = user_line.split('|')[0]
                if stored_username == username:
                    print("Error: Username already exists. Please choose another.")
                    self.pause()
                    return False

# Get password
            password = input("Enter password: ").strip()
            if not password:
                print("Error: Password cannot be empty")
                self.pause()
                return False

# Save new user
            user_data = username + "|" + password
            if self.user_file.write_to_file(user_data):
                print("\nAccount created successfully for", username, "!")
                print("You can now login with your credentials.")
                self.pause()
                return True
            else:
                print("Error: Failed to create account")
                self.pause()
                return False

        except Exception as e:
            print("Error during signup:" + str(e))
            self.pause()
            return False


    def login(self):
# Authenticates existing user and checks credentials against stored user records

        self.clear_screen()
        print("\n", "*" * 60)
        print("LOGIN - VEHICLE RENTAL MANAGEMENT SYSTEM")
        print("*" * 50)

        username = input("Username: ").strip()
        password = input("Password: ").strip()

# Read all users from file
        users = self.user_file.read_from_file()

# Check credentials
        for user_line in users:
            if user_line.startswith("Username|"):  # Skip header
                continue
            parts = user_line.split('|')
            if len(parts) == 2:
                stored_username, stored_password = parts
                if stored_username == username and stored_password == password:
                    self.currentUser = username
                    print("\nWelcome", self.currentUser, "!")
                    self.pause()
                    return True

        print("\nInvalid credentials. Please try again.")
        self.pause()
        return False


    def authentication_menu(self):
# Shows signup/login options at program start
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            self.clear_screen()
            print("\n", "*" * 60)
            print("VEHICLE RENTAL MANAGEMENT SYSTEM")
            print("*" * 60)
            print("1. Login")
            print("2. Signup (Create New Account)")
            print("3. Exit")
            print("*" * 60)

            choice = input("Select option (1-3): ").strip()

            if choice == '1':
                if self.login():
                    return True
                attempts += 1
            elif choice == '2':
                self.signup()
# After signup, loop back to let them Login
            elif choice == '3':
                print("\nExiting system. Goodbye!")
                return False
            else:
                print("Invalid option. Please select 1, 2, or 3.")
                self.pause()

        print("\nMaximum login attempts reached. Exiting system.")
        return False

# MAIN MENU SYSTEM

    def display_menu(self):
# Displays the main menu options
        self.clear_screen()
        print("\n", "*" * 60)
        print("MAIN MENU")
        print("*" * 60)
        print("1. Manage Vehicles")
        print("2. Manage Customers")
        print("3. Manage Rentals")
        print("4. Manage Payments")
        print("5. Generate Reports")
        print("6. Logout")
        print("*" * 60)


    def handle_user_choice(self, choice):
# Routes user to appropriate menu based on selection

        try:
            if choice == '1':
                self.manage_vehicles()
            elif choice == '2':
                self.manage_customers()
            elif choice == '3':
                self.manage_rentals()
            elif choice == '4':
                self.manage_payments()
            elif choice == '5':
                self.generate_reports()
            elif choice == '6':
                return False  # Logout signal
            else:
                print("Invalid option. Please select 1-6.")
                self.pause()
            return True
        except Exception as e:
            print("An error occurred:", str(e))
            self.pause()
            return True

# HELPER METHODS (Reduce Repetition)

    def get_entity_by_id(self, file_manager, entity_id, entity_class, entity_name):
# Generic method to retrieve any entity by ID and reduces code duplication across vehicle/customer/rental lookups

        data = file_manager.search_by_id(entity_id)
        if not data:
            print(entity_name, "not found")
            return None
        return entity_class.from_string(data)

    def show_submenu(self, title, options):
        """
        Displays a generic submenu with given title and options
        Returns user's choice
        """
        self.clear_screen()
        print("\n---" + title + "---")
        for i, option in enumerate(options, 1):
            print(i, ".", option)
        return input("Select option: ").strip()

# VEHICLE MANAGEMENT

    def manage_vehicles(self):
# Submenu for vehicle operations

        options = [
            "Add New Vehicle",
            "View All Vehicles",
            "Update Vehicle",
            "Remove Vehicle",
            "Search Vehicle by ID",
            "Back to Main Menu"
        ]

        choice = self.show_submenu("Vehicle Management", options)

        if choice == '1':
            self.add_vehicle()
        elif choice == '2':
            self.view_all_vehicles()
        elif choice == '3':
            self.update_vehicle()
        elif choice == '4':
            self.remove_vehicle()
        elif choice == '5':
            self.search_vehicle()

        if choice != '6':
            self.pause()

    def add_vehicle(self):
# Adds a new vehicle to the system

        try:
            print("\n--- Add New Vehicle ---")
            vehicle_id = input("Enter Vehicle ID: ").strip()

            if not vehicle_id or self.vehicle_file.search_by_id(vehicle_id):
                print("Error: Invalid or duplicate Vehicle ID")
                return

            vehicle_type = input("Enter Vehicle Type (Sedan/SUV/Truck): ").strip()
            brand = input("Enter Brand: ").strip()
            rental_rate = float(input("Enter Rental Rate per day ($): "))

            if rental_rate <= 0:
                print("Error: Rental rate must be positive")
                return

            vehicle = Vehicle(vehicle_id, vehicle_type, brand, rental_rate)

            if self.vehicle_file.write_to_file(vehicle.to_string()):
                print("Vehicle added successfully!")
                vehicle.display_details()
            else:
                print("Failed to add vehicle")

        except ValueError:
            print("Error: Invalid input. Please enter correct data types.")
        except Exception as e:
            print("Error:", str(e))

    def view_all_vehicles(self):
# Displays all vehicles in the system

        print("\n--- All Vehicles ---")
        lines = self.vehicle_file.read_from_file()

        if not lines or len(lines) <= 1:  # Empty or only header
            print("No vehicles found.")
            return

        for line in lines:
            if line.startswith("VehicleID|"):  # Skip header
                continue
            vehicle = Vehicle.from_string(line)
            if vehicle:
                vehicle.display_details()

    def update_vehicle(self):
# Updates vehicle information

        try:
            vehicle_id = input("Enter Vehicle ID to update: ").strip()
            vehicle = self.get_entity_by_id(self.vehicle_file, vehicle_id, Vehicle, "Vehicle")

            if not vehicle:
                return

            vehicle.display_details()

            print("\n1. Update Rental Rate")
            print("2. Update Vehicle Status")
            choice = input("Select option: ")

            if choice == '1':
                new_rate = float(input("Enter new rental rate: "))
                vehicle.rentalRate = new_rate
            elif choice == '2':
                print("Status: 1-Available, 2-Rented, 3-Maintenance")
                status_map = {'1': 'Available', '2': 'Rented', '3': 'Maintenance'}
                status_choice = input("Choice: ")
                if status_choice in status_map:
                    vehicle.set_availability_status(status_map[status_choice])

            if self.vehicle_file.update_file(vehicle_id, vehicle.to_string()):
                print("Vehicle updated successfully!")

        except Exception as e:
            print("Error:", str(e))

    def remove_vehicle(self):
# Removes a vehicle from the system

        vehicle_id = input("Enter Vehicle ID to remove: ").strip()
        if self.vehicle_file.delete_from_file(vehicle_id):
            print("Vehicle removed successfully!")
        else:
            print("Vehicle not found")

    def search_vehicle(self):
# Searches for a vehicle by ID

        vehicle_id = input("Enter Vehicle ID: ").strip()
        vehicle = self.get_entity_by_id(self.vehicle_file, vehicle_id, Vehicle, "Vehicle")
        if vehicle:
            vehicle.display_details()

# CUSTOMER MANAGEMENT

    def manage_customers(self):
# Submenu for customer operations

        options = [
            "Add New Customer",
            "View All Customers",
            "Update Customer",
            "Remove Customer",
            "Search Customer by ID",
            "Back to Main Menu"
        ]

        choice = self.show_submenu("Customer Management", options)

        if choice == '1':
            self.add_customer()
        elif choice == '2':
            self.view_all_customers()
        elif choice == '3':
            self.update_customer()
        elif choice == '4':
            self.remove_customer()
        elif choice == '5':
            self.search_customer()

        if choice != '6':
            self.pause()

    def add_customer(self):
# Adds a new customer

        try:
            print("\n--- Add New Customer ---")
            customer_id = input("Enter Customer ID: ").strip()

            if not customer_id or self.customer_file.search_by_id(customer_id):
                print("Error: Invalid or duplicate Customer ID")
                return

            name = input("Enter Customer Name: ").strip()
            contact = input("Enter Contact Details: ").strip()
            license = input("Enter License Number: ").strip()

            if not license:
                print("Error: License number is required")
                return

            customer = Customer(customer_id, name, contact, license)

            if self.customer_file.write_to_file(customer.to_string()):
                print("Customer added successfully!")
                customer.display_details()

        except Exception as e:
            print("Error:", str(e))

    def view_all_customers(self):
# Displays all customers

        print("\n--- All Customers ---")
        lines = self.customer_file.read_from_file()

        if not lines or len(lines) <= 1:
            print("No customers found.")
            return

        for line in lines:
            if line.startswith("CustomerID|"):
                continue
            customer = Customer.from_string(line)
            if customer:
                customer.display_details()

    def update_customer(self):
# Updates customer information

        try:
            customer_id = input("Enter Customer ID to update: ").strip()
            customer = self.get_entity_by_id(self.customer_file, customer_id, Customer, "Customer")

            if not customer:
                return

            customer.display_details()
            new_contact = input("\nEnter new contact (or press Enter to skip): ").strip()

            if new_contact:
                customer.contactDetails = new_contact
                if self.customer_file.update_file(customer_id, customer.to_string()):
                    print("Customer updated successfully!")

        except Exception as e:
            print("Error:", str(e))

    def remove_customer(self):
# Removes a customer

        customer_id = input("Enter Customer ID to remove: ").strip()
        if self.customer_file.delete_from_file(customer_id):
            print("Customer removed successfully!")
        else:
            print("Customer not found")

    def search_customer(self):
# Searches for a customer by ID

        customer_id = input("Enter Customer ID: ").strip()
        customer = self.get_entity_by_id(self.customer_file, customer_id, Customer, "Customer")
        if customer:
            customer.display_details()






