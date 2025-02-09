import bcrypt


def password_hash(password):
    """
    Hashes a password using bcrypt.
    Args:
        password (str): The password to hash.
    Returns:
        bytes: The hashed password.
    """
    # Generate a salt with specified rounds
    salt = bcrypt.gensalt(rounds=15)

    # Hash the password (must encode to bytes)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def verify_password(password, hashed_password):
    """
    Verifies a password against its hashed value.
    Args:
        password (str): The plaintext password to check.
        hashed_password (bytes or str): The hashed password to compare against.
    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    # If the hashed password is a string, encode it to bytes
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')

    # Encode the input password to bytes
    password_utf = password.encode('utf-8')

    # Check the password and return the result
    return bcrypt.checkpw(password_utf, hashed_password)