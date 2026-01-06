
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, brand, rental_rate, status="Available"):
        # basic vehicle details
        self.vehicleID = vehicle_id
        self.type = vehicle_type
        self.brand = brand
        self.rentalRate = rental_rate
        self.status = status

    def get_status(self):

    # return current vehicle status
        return self.status

    def set_status(self, new_status):

    # change vehicle status if valid
        if new_status == "Available" or new_status == "Rented" or new_status == "Maintenance":
            self.status = new_status
            return True
        else:
            return False

    def to_file_string(self):

        # convert vehicle data to string for saving in file
        return self.vehicleID + "|" + self.type + "|" + self.brand + "|" + str(self.rentalRate) + "|" + self.status

    @staticmethod
    def from_file_string(line):
        # create vehicle object from file data
        parts = line.strip().split("|")
        if len(parts) == 5:
            return Vehicle(parts[0], parts[1], parts[2], float(parts[3]), parts[4])
        return None

    def show_vehicle(self):

        # display vehicle details
        print("Vehicle ID:", self.vehicleID)
        print("Type:", self.type)
        print("Brand:", self.brand)
        print("Rental Rate:", self.rentalRate)
        print("Status:", self.status)
