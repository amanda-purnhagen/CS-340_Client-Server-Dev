from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the  
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30235
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    def test_print(self):
        return f'Test print successful.'

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data) # data should be dictionary
                return True #The data insert was successful
            except Exception as e:
                print(f"Failed to insert data: {e}")
                return False # The data insert was not successful
        else:
            raise Exception("Nothing to save, because data parameter is empty")


# Create method to implement the R in CRUD.
    def read(self, lookup_dictionary):
        try:
            result = list(self.collection.find(lookup_dictionary))
            #result_string = str(result[0])
            #for item in result:
                #result_string = result_string + "\n\n" + str(item)
            #return result_string # Print, in string format, the result if the read command is successful
            return result # Updated to support the return of a list object
        except Exception as e:
            print(f"Failed to read data: {e}")
            return [] # Return an empty list if the read command is unsuccessful
        
# Create method to implement the U in CRUD.
    def update(self, lookup_data, update_key, update_value):
        try:
            result = self.collection.update_many(lookup_data, {"$set": { update_key : update_value }})
            return result.modified_count # Return the number of modified objects if successful
        except Exception as e:
            print(f"Failed to read data: {e}")
            
# Create method to implement the D in CRUD.
    def delete(self, lookup_key, lookup_value):
        try:
            result = self.collection.delete_many({ lookup_key : lookup_value })
            return result.deleted_count # Return the number of deleted objects if successful
        except Exception as e:
            print(f("Failed to delete data with lookup key/value pair: " + lookup_key + " : " + 
                  lookup_value + "."))