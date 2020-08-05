from dbconnect import create_connection


def delete_one(param, collection_name):
    my_collection = create_connection(collection_name)
    my_collection.delete_one(param)
