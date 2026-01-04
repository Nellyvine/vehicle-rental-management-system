"""
Vehicle Class - Manages vehicle details and availability status
This class represents a single vehicle in the rental system
"""

class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, brand, rental_rate, status="Available"):
        """
        Initialize a new vehicle with all required details
        Status can be: Available, Rented, or Maintenance
        """
        self.vehicleID = vehicle_id
        self.type = vehicle_type
        self.brand = brand
        self.rentalRate = rental_rate
        self.status = status
    
    def get_availability_status(self):
        """Returns the current availability status of the vehicle"""
        return self.status
    
    def set_availability_status(self, new_status):
        """
        Updates the vehicle status
        Used when vehicle is rented, returned, or needs maintenance
        """
        valid_statuses = ["Available", "Rented", "Maintenance"]
        if new_status in valid_statuses:
            self.status = new_status
            return True
        else:
            return False
    
    def to_string(self):
        """
        Converts vehicle data to a string format for file storage
        Format: ID|Type|Brand|Rate|Status
        """
        return f"{self.vehicleID}|{self.type}|{self.brand}|{self.rentalRate}|{self.status}"
    
    @staticmethod
    def from_string(data_string):
        """
        Creates a Vehicle object from a stored string
        This is used when reading vehicles from file
        """
        parts = data_string.strip().split('|')
        if len(parts) == 5:
            return Vehicle(parts[0], parts[1], parts[2], float(parts[3]), parts[4])
        return None
    
    def display_details(self):
        """Displays vehicle information in a readable format"""
        print(f"\n--- Vehicle Details ---")
        print(f"Vehicle ID: {self.vehicleID}")
        print(f"Type: {self.type}")
        print(f"Brand: {self.brand}")
        print(f"Rental Rate: ${self.rentalRate} per day")
        print(f"Status: {self.status}")
        print(f"----------------------")