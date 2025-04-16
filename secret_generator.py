import string
import random

def generate_secret(length=32):
    """Generate a random alphanumeric secret of the given length."""
    characters = string.ascii_letters + string.digits
    secret = ''.join(random.choice(characters) for _ in range(length))
    return secret

if __name__ == "__main__":
    secret = generate_secret()
    print("Random alphanumeric secret:", secret)