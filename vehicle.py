
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, brand, rental_rate, status="Available"):
        # store vehicle information
        self.vehicleID = vehicle_id
        self.type = vehicle_type
        self.brand = brand
        self.rentalRate = rental_rate
        self.status = status

        def get_availability_status(self):
            return self.status

        def set_availability_status(self, new_status):
            if new_status == "Available" or new_status == "Rented" or new_status == "Maintenance":
                self.status = new_status
                return True
            else:
                return False

    def to_string(self):
        return self.vehicleID + "|" + self.type + "|" + self.brand + "|" + str(self.rentalRate) + "|" + self.status

    @staticmethod
    def from_string(data_string):
        parts = data_string.strip().split('|')
        if len(parts) == 5:
            return Vehicle(parts[0], parts[1], parts[2], float(parts[3]), parts[4])
        return None

    def display_details(self):
        print("\n--- Vehicle Details ---")
        print("Vehicle ID:", self.vehicleID)
        print("Type:", self.type)
        print("Brand:", self.brand)
        print("Rental Rate:", self.rentalRate)
        print("Status:", self.status)
        print("----------------------")
