import time
import phonenumbers

from pymongo import MongoClient
from faker import Factory
from faker.providers.phone_number.en_US import Provider

#
# client = MongoClient('mongodb://user:pass@host.domain.com:23325/db')
# db = client.db

class CustomPhoneProvider(Provider):
    def phone_number(self):
        while True:
            phone_number = self.numerify(self.random_element(self.formats))
            parsed_number = phonenumbers.parse(phone_number, 'US')
            if phonenumbers.is_valid_number(parsed_number):
                return phonenumbers.format_number(
                    parsed_number,
                    phonenumbers.PhoneNumberFormat.E164
                )


def create_data(fake):
    """creates 10 fake data phone number of region us"""
    fake.add_provider(CustomPhoneProvider)
    for x in range(10):
        generated_name = fake.first_name()
        generated_surname = fake.last_name()
        phone_number = fake.phone_number()
        address = fake.address()
        # balance = fake

        # result = db.col1.insert_one(
        #             {
        #                 'name': genName,
        #                 'surname': genSurname,
        #                 'job': genJob,
        #                 'country': genCountry
        #                 }
        #             )

        d = {'name': generated_name,
             'surname': generated_surname,
             'phone_number': phone_number,
             'address': address}

        print (d)
        # time.sleep(1)

if __name__ == '__main__':
    fake = Factory.create('en_US')
    create_data(fake)