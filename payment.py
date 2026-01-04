# Payment class will manage payment details for rentals

class Payment:
    def __init__(self, payment_id, rental_id, amount_paid, payment_date):
# Initialize a new payment record
        self.paymentID = payment_id
        self.rentalID = rental_id
        self.amountPaid = amount_paid
        self.paymentDate = payment_date

    def validate_payment(self, expected_amount):
# Validates if payment amount matches the expected rental cost
        try:
            if self.amountPaid < 0:
                raise ValueError("Payment amount cannot be negative")

            if self.amountPaid >= expected_amount:
                return True
            else:
                return False
        except ValueError as e:
            raise ValueError("Payment validation error: " + str(e))
