from utils.server.CRUD_Users import find_user
from utils.server.CRUD_Location import find_location
import random
import string

def generate_unique_id(type=None):
    """generates a unique id, which is a string (10 letters long)"""
    while True:
        # unique id generation (k=10 is the length of the random string)
        unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        # Check if ID is already taken (reliability reason)
        # if ID is randomly same, the app will encounter issues

        # check user id
        if type == "user":
            # uses find_user from the CRUD_Users.py file
            if not find_user("id", unique_id):
                print("Unique ID - No User found")
                return unique_id  # if no user is found, then return
            else:
                print(f"ID {unique_id} already exists. Generating a new one...")
                # if a user is found, the while statement will loop and print out this message (still debugging)

        # check location id
        elif type == "location":
            if not find_location("id", unique_id):
                print("Unique ID - No Location found")
                return unique_id  # if no user is found, then return
            else:
                print(f"ID {unique_id} already exists. Generating a new one...")
                # if a user is found, the while statement will loop and print out this message (still debugging)

        # random unique id without checking (needs to be added), but at the moment it should work without (length 10 with 26 Letters and 10 digits - same id should be very rare)
        elif type == "random":
            #security issue here
            return unique_id