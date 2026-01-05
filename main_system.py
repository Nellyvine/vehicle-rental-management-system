# MainSystem Class, Controls overall program flow and user interaction

class MainSystem:
    def __init__(self):
        self.currentUser = None
        self.vehicle_file = FileManager("vehicles.txt")
        self.customer_file = FileManager("customers.txt")
        self.rental_file = FileManager("rentals.txt")
        self.payment_file = FileManager("payments.txt")
        self.user_file = FileManager("users.txt")

# Initialize files with headers
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