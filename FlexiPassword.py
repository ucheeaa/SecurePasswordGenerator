import secrets
import string

# User is asked how many Capital letters they want
# If yes they get to choose how many they want. Must be a minimum of 1 for password security
# Error handling was done here as well
def number_of_passwords_generated() -> int:

    while True:
        try:
            no_password_generated = int(input("How many passwords should be generated? "))
            return no_password_generated
        except ValueError:
            print(f"Invalid input. Please enter a valid whole number.")


def input_base_word():
    while True:
        # User inputs base word
        user_inputs_base_word = input(
            "Enter your password base word. This must contain only letters and must be at least 1 letter.: ")
        base_word_without_spaces = user_inputs_base_word.replace(" ", "")

        # Validate that the input contains only letters
        if not base_word_without_spaces.isalpha():
            print("Invalid input. The base word must contain only letters.")
        else:
            # Converts base word to lower case letters and removes unnecessary spaces.
            lowercase_base_word_without_spaces = base_word_without_spaces.lower()
            length_of_base_word = len(lowercase_base_word_without_spaces)
            break
    return lowercase_base_word_without_spaces, length_of_base_word

def remaining_characters_for_strength(length_of_base_word):

    remaining_characters = 12 - length_of_base_word  # to make password strong enough
    return remaining_characters


def capital_characters():
    while True:
        try:
            no_of_capitals = int(input(
                "Do you want to choose the number of capitals you want in the passwords? Reply:  '1' for yes and '2' no: "))
            if no_of_capitals == 1 or no_of_capitals == 2:
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if no_of_capitals == 1:
        while True:
            try:
                num_capital_letters = int(input("How many capital letters do you want in your password? Must be a "
                                                "minimum of 1: "))
                if num_capital_letters >= 1:
                    return num_capital_letters
                else:
                    print(
                        "Invalid input. There must be 1 or more capital letters in your password")
            except ValueError:
                print("Invalid input. Please enter a valid whole number.")
    else:
        return -1  # The user doesn't mind the number of capital letters in the password.

def number_of_special_characters_and_numbers(length_of_base_word):
    remaining_characters = remaining_characters_for_strength(length_of_base_word)
    if length_of_base_word >= 12:
        while True:
            try:
                no_of_special_characters = int(
                    input("How many special characters should your password contain? Must be a "
                          "minimum of 1 :"))
                if no_of_special_characters >= 1:
                    break
                else:
                    print(
                        "Invalid input. There must be 1 or more special_characters in your password")
            except ValueError:
                print("Invalid input. Please enter a valid whole number.")
    else:
        print(f"Given your base word has {length_of_base_word} characters; The number of numbers and special "
              f"characters you want in your password has to be equals to or greater than {remaining_characters}.")
        while True:
            try:
                no_of_special_characters = int(
                    input("How many special characters do you want your password to contain?: "))
                if no_of_special_characters >= 1:
                    break
                else:
                    print(
                        "Invalid input. There must be 1 or more special_characters in your password")
            except ValueError:
                print("Invalid input. Please enter a valid whole number.")

    if length_of_base_word >= 12:
        while True:
            try:
                no_of_numbers = int(
                    input("How many numbers should your password contain? Must be a "
                          "minimum of 1 :"))
                if no_of_numbers >= 1:
                    break
                else:
                    print(
                        "Invalid input. There must be 1 or more numbers in your password")
            except ValueError:
                print("Invalid input. Please enter a valid whole number.")

    else:
        min_num = remaining_characters - no_of_special_characters
        if min_num <= 0:
            print("Your password already contains 12 characters including the special characters. You just have to "
                  "pick one or more numbers for you password to make it strong enough.")
            while True:
                try:
                    no_of_numbers = int(
                        input("How many numbers should your password contain? "))
                    if no_of_numbers >= 1:
                        break
                    else:
                        print(
                            "Invalid input. There must be 1 or more numbers in your password")
                except ValueError:
                    print("Invalid input. Please enter a valid whole number greater than or equals to one.")
        else:
            print(f"Your password now contains {length_of_base_word + no_of_special_characters} characters including "
                  f"the special characters. You just have to "
                  f"pick {min_num} or more numbers for your password to make it strong enough.")
            while True:
                try:
                    no_of_numbers = int(
                        input("How many numbers should your password contain?: "))
                    if no_of_numbers >= 1 and no_of_numbers >= min_num:
                        break
                    else:
                        print(
                             f"Invalid input. There must be {min_num} or more numbers in your password to make it strong enough")

                except ValueError:
                    print(f"Invalid input. Please enter a valid whole number greater than or equals to {min_num} to make you password strong enough")

    return no_of_special_characters, no_of_numbers

def generate_password(base_word, special_characters_count, numbers_count,num_same, sc_same):

    password_list = list(base_word)
    len_base_word= len(password_list)
    special_characters = string.punctuation

    numbers = string.digits
    if num_same == True and sc_same == True:
        for _ in range(special_characters_count):
            password_list.append(secrets.choice(special_characters))
        for _ in range(numbers_count):
            password_list.append(secrets.choice(numbers))
    elif num_same == True and sc_same == False:
        for _ in range(special_characters_count):
            password_list.append(secrets.choice(special_characters))

    elif num_same == False and sc_same == True:
        for _ in range(numbers_count):
            password_list.append(secrets.choice(numbers))

    return password_list, len_base_word

def all_shuffled_same_sc_num( amount: int, base_word, special_characters_count, numbers_count):

    password, len_base_word= generate_password(base_word, special_characters_count, numbers_count, True, True)
    passwords = []
    for _ in range(amount):
        secrets.SystemRandom().shuffle(password)
        shuffled_password = ''.join(password)
        passwords.append(shuffled_password)
    print (passwords)

def all_shuffled_diff_sc_num( amount: int, base_word, special_characters_count, numbers_count):

    passwords = []
    for _ in range(amount):
        password, len_base_word = generate_password(base_word, special_characters_count, numbers_count, True, True)
        secrets.SystemRandom().shuffle(password)
        shuffled_password = ''.join(password)
        passwords.append(shuffled_password)
    print (passwords)

def all_shuffled_diff_sc_same_num(amount: int, base_word, special_characters_count, numbers_count):
    passwords = []
    numbers = []
    for _ in range(numbers_count):
        numbers.append(secrets.choice(string.digits))

    for _ in range(amount):
        generated_password_without_digits, len_base_word = generate_password(base_word, special_characters_count, numbers_count, True, False)
        password = numbers + generated_password_without_digits
        secrets.SystemRandom().shuffle(password)
        shuffled_password = ''.join(password)
        passwords.append(shuffled_password)
    print (passwords)

def all_shuffled_same_sc_diff_num(amount: int, base_word, special_characters_count, numbers_count):
    passwords = []
    special_characters = []
    for _ in range(special_characters_count):
        special_characters.append(secrets.choice(string.punctuation))

    for _ in range(amount):
        generated_password_without_digits, len_base_word = generate_password(base_word, special_characters_count, numbers_count, False,
                                                              True)
        password = special_characters + generated_password_without_digits
        secrets.SystemRandom().shuffle(password)
        shuffled_password = ''.join(password)
        passwords.append(shuffled_password)
    print (passwords)


def base_word_not_shuffled_same_sc_num( amount: int, base_word, special_characters_count, numbers_count):
    password, len_base_word = generate_password(base_word, special_characters_count, numbers_count, True, True)
    len_password = len(password)
    slice = len_base_word
    password_without_sc_and_num = password[:slice] # Slices from the start up to (but not including) the index 'slice'.
    sc_and_num = password[slice:]  # Slices from the index 'slice' to the end
    number_list = list(range(len_password + 2))

    passwords = []
    for _ in range(amount):
        sc_num_new_index = [secrets.choice(number_list) for _ in range(len(sc_and_num))]
        passs=password_without_sc_and_num[:]
        print(passs)
        for i in range(len(sc_and_num)):
            passs.insert(sc_num_new_index[i],sc_and_num[i])
        password_with_sc_num = passs[:]
        password_with_sc_num_string = ''.join(password_with_sc_num)
        passwords.append(password_with_sc_num_string)
    print (passwords)

def base_word_not_shuffled_diff_sc_num( amount: int, base_word, special_characters_count, numbers_count):
    passwords = []
    for _ in range(amount):
        password, len_base_word = generate_password(base_word, special_characters_count, numbers_count, True, True)
        len_password = len(password)
        slice = len_base_word
        password_without_sc_and_num = password[
                                      :slice]  # Slices from the start up to (but not including) the index 'slice'.
        sc_and_num = password[slice:]  # Slices from the index 'slice' to the end
        number_list = list(range(len_password + 2))

        sc_num_new_index = [secrets.choice(number_list) for _ in range(len(sc_and_num))]
        passs=password_without_sc_and_num[:]

        for i in range(len(sc_and_num)):
            passs.insert(sc_num_new_index[i],sc_and_num[i])
        password_with_sc_num = passs[:]
        password_with_sc_num_string = ''.join(password_with_sc_num)
        passwords.append(password_with_sc_num_string)
    print (passwords)



def choose_flexi_password_type():
    print("Choose the type of FlexiPassword you want to generate:")
    print("1. All Shuffled with Same Special Characters and Numbers")
    print("2. All Shuffled with Different Special Characters and Numbers")
    print("3. All Shuffled with Different Special Characters but Same Numbers")
    print("4. All Shuffled with Same Special Characters but Different Numbers")
    print("5. Base Word Not Shuffled with Same Special Characters and Numbers")
    print("6. Base Word Not Shuffled with Different Special Characters and Numbers")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


mine = base_word_not_shuffled_same_sc_num( 5, 'uche', 5,5)
print (mine)


