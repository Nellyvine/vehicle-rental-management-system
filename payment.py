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
            raise ValueError("Payment validation error: ", + str(e))

    def process_payment(self):
# Processes the payment
        if self.amountPaid > 0:
            return True
        return False

    def get_payment_details(self):
# Returns payment information as a dictionary
        return {
            'paymentID': self.paymentID,
            'rentalID': self.rentalID,
            'amountPaid': self.amountPaid,
            'paymentDate': self.paymentDate
        }

    def to_string(self):
# Converts payment data to string format for file storage
# Format: PaymentID|RentalID|AmountPaid|PaymentDate
        return f"{self.paymentID}|{self.rentalID}|{self.amountPaid}|{self.paymentDate}"

    @staticmethod
    def from_string(data_string):
# Creates a Payment object from a stored string used when loading payments from file
        parts = data_string.strip().split('|')
        if len(parts) == 4:
            return Payment(parts[0], parts[1], float(parts[2]), parts[3])
        return None

    def display_details(self):
# Displays payment information in a readable format
        print("\n--- Payment Details ---")
        print("Payment ID:", self.paymentID)
        print("Rental ID:", self.rentalID)
        print("Amount Paid: %.2f" % self.amountPaid)
        print("Payment Date:", self.paymentDate)
        print("--------------------------")