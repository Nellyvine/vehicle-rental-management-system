from datetime import datetime

class Rental:
    def __init__(self, rental_id, customer_id, vehicle_id, rental_date, return_date=None, total_cost=0.0):
        # basic rental details
        self.rentalID = rental_id
        self.customerID = customer_id
        self.vehicleID = vehicle_id
        self.rentalDate = rental_date
        self.returnDate = return_date
        self.totalCost = total_cost


    def calculate_rental_cost(self, rental_rate):
        # calculate total cost using rental dates
        start_date = datetime.strptime(self.rentalDate, "%Y-%m-%d")
        end_date = datetime.strptime(self.returnDate, "%Y-%m-%d")

        days = (end_date - start_date).days

        if days <= 0:
            return False

        self.totalCost = days * rental_rate
        return self.totalCost

    def close_rental(self, return_date):

        # set return date when vehicle is returned
        self.returnDate = return_date
        return True

    def get_rental_details(self):

        # return rental details
        return {
            "rentalID": self.rentalID,
            "customerID": self.customerID,
            "vehicleID": self.vehicleID,
            "rentalDate": self.rentalDate,
            "returnDate": self.returnDate,
            "totalCost": self.totalCost
        }

    def to_string(self):

        # convert rental data to string for file storage
        if self.returnDate is None:
            return_date = "Active"
        else:
            return_date = self.returnDate

        return (
            self.rentalID + "|" +
            self.customerID + "|" +
            self.vehicleID + "|" +
            self.rentalDate + "|" +
            return_date + "|" +
            str(self.totalCost)
        )

    @staticmethod
    def from_string(data_string):

        # create rental object from file data
        parts = data_string.strip().split("|")
        if len(parts) == 6:
            return_date = None if parts[4] == "Active" else parts[4]
            return Rental(parts[0], parts[1], parts[2], parts[3], return_date, float(parts[5]))
        return None


    def display_details(self):

        # display rental information
        print("Rental ID:", self.rentalID)
        print("Customer ID:", self.customerID)
        print("Vehicle ID:", self.vehicleID)
        print("Rental Date:", self.rentalDate)
        print("Return Date:", self.returnDate if self.returnDate else "Not yet returned")
        print("Total Cost:", self.totalCost)
