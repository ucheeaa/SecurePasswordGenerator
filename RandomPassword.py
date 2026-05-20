import secrets
import string

def comp_password(pass_length: int) -> str:
    try:
        if pass_length < 4:
            raise ValueError("Password length must be at least 4 to meet security requirements.")

        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        required_chars = [
            secrets.choice(string.ascii_uppercase),  # At least one capital letter
            secrets.choice(string.ascii_lowercase),  # At least one small letter
            secrets.choice(digits),                  # At least one digit
            secrets.choice(special_chars)            # At least one special character
        ]

        remaining_length = pass_length - len(required_chars)
        additional_chars = [secrets.choice(letters + digits + special_chars) for _ in range(remaining_length)]

        all_chars = required_chars + additional_chars
        secrets.SystemRandom().shuffle(all_chars)

        password = ''.join(all_chars)
        return password
    except ValueError as e:
        return str(e)






     
    
    
