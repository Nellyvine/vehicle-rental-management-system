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
