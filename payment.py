# Payment class will manage payment details for rentals

class Payment:
    def __init__(self, payment_id, rental_id, amount_paid, payment_date):
        self.payment_id = payment_id
        self.rental_id = rental_id
        self.amount_paid = amount_paid
        self.payment_date = payment_date

