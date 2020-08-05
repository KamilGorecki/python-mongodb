from dbconnect import create_connection
import bcrypt


def hash_password(password_to_hashed):
    hashed_password = bcrypt.hashpw(password_to_hashed, bcrypt.gensalt(10, prefix=b"2a"))
    return hashed_password.decode('utf-8')


def create_doc(doc, collection_name):
    my_collection = create_connection(collection_name)
    password = hash_password(doc['pass'].encode())
    doc['pass'] = password
    my_collection.insert_one(doc)
