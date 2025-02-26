import bcrypt


def password_hash(password):
    """
    Password hash encrypts the password using bcrypt
    """
    # Salt - random value "added" to the string
    salt = bcrypt.gensalt(rounds=15)

    # converting the password to utf-8 and hashes the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def verify_password(password, hashed_password):
    """
    decrypts the password and combines it with the given password
    """
    # hased_password is stored as string in mongodb - deconverting
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')

    # encodes the new input password to utf-8
    password_utf = password.encode('utf-8')

    # checks the password using bcrypt
    return bcrypt.checkpw(password_utf, hashed_password)