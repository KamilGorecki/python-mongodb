import pymongo


def create_connection(collection):
    myclient = pymongo.MongoClient(
        "mongodb://...../", retryWrites=False)
    mydb = myclient["maindb"]
    my_collection = mydb[collection]
    return my_collection
