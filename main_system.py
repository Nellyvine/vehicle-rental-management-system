# MainSystem Class, Controls overall program flow and user interaction

from file_manager import FileManager
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
                print("\nAccount created successfully for" + username +"!")
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
        print("\n" + "*" * 60)
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
                    print("\nWelcome" + self.currentUser + "!")
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
            print("\n" + "*" * 60)
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
# After signup, loop back to let them login
            elif choice == '3':
                print("\nExiting system. Goodbye!")
                return False
            else:
                print("Invalid option. Please select 1, 2, or 3.")
                self.pause()

        print("\nMaximum login attempts reached. Exiting system.")
        return False



