from datetime import datetime


def generate_valid_email():
    user_email = f'test_email{datetime.utcnow().strftime("%Y%m%d-%H%M%S")}@example.com'
    return user_email


def get_valid_password():
    password = "Passw0rd1!!"
    return password


def get_weak_password():
    password = "123456789"
    return password
