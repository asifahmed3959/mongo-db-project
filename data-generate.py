import time

from pymongo import MongoClient
from faker import Factory

#
# client = MongoClient('mongodb://user:pass@host.domain.com:23325/db')
# db = client.db


def create_data(fake):
    """creates 10 fake data"""

    for x in range(10):
        generated_name = fake.first_name()
        generated_surname = fake.last_name()
        phone_number = fake.phone_number()
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
             'job': phone_number}

        print (d)
        # time.sleep(1)

if __name__ == '__main__':
    fake = Factory.create()
    create_data(fake)