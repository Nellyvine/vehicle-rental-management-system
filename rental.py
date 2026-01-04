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
