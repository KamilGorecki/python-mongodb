from dbconnect import create_connection


def read_all(collection_name):
    my_collection = create_connection(collection_name)
    for doc in my_collection.find():
        print(doc)
