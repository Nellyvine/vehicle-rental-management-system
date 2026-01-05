
class Customer:
    def __init__(self, customer_id, name, contact_details, license_number):

        # Basic customer information
        self.customerID = customer_id
        self.name = name
        self.contactDetails = contact_details
        self.licenseNumber = license_number

    def get_customer_details(self):

        return {
            'customerID': self.customerID,
            'name': self.name,
            'contactDetails': self.contactDetails,
            'licenseNumber': self.licenseNumber
        }


    def to_string(self):
        return self.customerID + "|" + self.name + "|" + self.contactDetails + "|" + self.licenseNumber


    @staticmethod

    def from_string(data_string):
        parts = data_string.strip().split('|')
        if len(parts) == 4:

            return Customer(parts[0], parts[1], parts[2], parts[3])
        return None
