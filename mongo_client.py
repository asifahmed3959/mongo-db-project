import uuid
import pymongo
from faker import Faker
from random import randint


# connect to db
client = pymongo.MongoClient(
    "mongodb+srv://*********:********@cluster0.ovfat.mongodb.net/cse716?retryWrites=true&w=majority")
db = client.cse716
collection = db["collection1"]


# =====     Insert Data    =====
def insert_n(n):
    for _ in range(n):
        row = faker_()
        print("adding data ", row)
        collection.insert_one(row)


def insert_one():
    row = faker_()
    print("adding data ", row)
    collection.insert_one(row)


# =====     Retrieve Data    =====
def retrieve(key, value):
    results = collection.find_one({key: value})
    print(results)


# =====     Update Data     =====
def update_entry(id, key, value):
    collection.update_one({"_id": id}, {"$set": {key: value}})


# =====     Update multiple fields in a row     =====
def update_multiple_fields_of_a_document(id, key_value_pairs):
    collection.update_one({"_id": id}, {"$set": key_value_pairs})


# === remove the field defined from all the rows ====
def remove_specific_field_from_all_rows(key):
    collection.update({}, {"$unset": {key:""} } , {"multi": True})


# === add one to phone number after 017 ===
def add_one_to_phone_number(phone_number): #0172233667
    if phone_number is None:
        return
    return phone_number[:3] + str(1) + phone_number[3:] #01712233667


# == splits name into first name and last name ===
def split_name(name): # Asif Ahmed Jr
    splitted_name = name.split() #['Asif', 'Ahmed', 'Jr']
    first_name = splitted_name.pop(0) # 'Asif'
    last_name = " ".join(splitted_name) # 'Ahmed Jr'
    return first_name, last_name


# =====     Delete one row     =====
def delete_one(key, value):
    collection.delete_one({key: value})


# =====     Get count of row     =====
def get_count():
    post_count = collection.count_documents({})
    print(post_count)


def faker_():
    fake_entry = {"_id": None, "name": None, "addr": None, "nid": None, "brthcrt": None, "phone": None}
    fake = Faker()
    id = uuid.uuid4()
    id = str(id)
    phone = "017"
    phone = phone + str(randint(1000000, 9999999))

    fake_entry.update({"_id": randint(100000, 999999)})
    fake_entry.update({"name": fake.name()})
    fake_entry.update({"addr": fake.address()})
    fake_entry.update({"nid": fake.ssn()})
    fake_entry.update({"brthcrt": str(randint(10000000, 99999999))})
    fake_entry.update({"phone": phone})

    return fake_entry


# iterate through the objects and update them
def iterate_rows():
    for x in collection.find():
        new_phone_number=add_one_to_phone_number(x['phone'])
        first_name, last_name = split_name(x['name'])
        data = {
            'phone' : new_phone_number,
            'first_name' : first_name,
            'last_name' : last_name
        }
        update_multiple_fields_of_a_document(id=x['_id'], key_value_pairs=data)
        remove_specific_field_from_all_rows('name')


def main():
    # id = 464391
    # key = "phone"
    # value = "0175356443"
    # update_entry(id, key, value)
    # retrieve(key, value)
    # insert_n(5)
    get_count()
    # iterate_rows()
    client.close()


if __name__ == "__main__":
    main()