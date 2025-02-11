from utils.server.CRUD_Users import find_user
from utils.server.CRUD_Location import find_location
import random
import string

def generate_unique_id(type):
    """Generates a unique ID that does not already exist in the database."""
    while True:
        # generate an ID which is 10 letters long (k=10)
        unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        if type == "user":
            # uses find_user from the CRUD_Users.py file
            if not find_user("id", unique_id):
                print("Unique ID - No User found")
                return unique_id  # if no user is found, then return
            else:
                print(f"ID {unique_id} already exists. Generating a new one...")
                # if a user is found, the while statement will loop and print out this message (still debugging)

        elif type == "location":
            if not find_location("id", unique_id):
                print("Unique ID - No Location found")
                return unique_id  # if no user is found, then return
            else:
                print(f"ID {unique_id} already exists. Generating a new one...")
                # if a user is found, the while statement will loop and print out this message (still debugging)