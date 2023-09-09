from RandomPassword import comp_password
import LexiPassword
import FlexiPassword
import secrets


print("Welcome to The Ultimate FlexiSecure Password Generator!\n")

print("Please follow the prompts and provide valid responses. Your input will help customize your password based on your preferences.\n")

user_choice = input('What kind of password generator do you want to use?\n '
                    '1. A Simple and Secure password generator that allows you to input a password '
                    'length, which must be greater than or equal to 4 and ensures \n    the inclusion of at '
                    'least one of each: a capital letter, a small letter, a number, and a special character.\n '
                    '2. A Flexible and Secure password generator that creates a strong password based on your '
                    'preferences for a base word\'s part of speech \n     the number of '
                    'capital letters, special characters, and numbers you desire.\n '
                    '3. A Flexible and Strong password generator that allows you to choose a base word, '
                    'the amount of capital letters, special characters, and numbers.')


if user_choice == "1":
    # Call the function for the Flexible Password Generator
    pass_length = int(input("Enter the desired password length greater or equals to 4: "))
    password = comp_password(pass_length)
    print("Generated Password:", password)

elif user_choice == "2":
    no_of_passwords = FlexiPassword.number_of_passwords_generated()
    selected_part = LexiPassword.choose_base_word_pos()  # Choose a part of speech
    words = LexiPassword.fetch_words_by_pos(selected_part)  # Fetch words based on the chosen part of speech
    base_word = secrets.choice(words)
    print (f"The base_word generated is {base_word}")
    length_of_base_word = len(base_word)
    # num_capital_letters = FlexiPassword.capital_characters()

    sc_amount, num_amount = FlexiPassword.number_of_special_characters_and_numbers(length_of_base_word)
    flexi_password_type = FlexiPassword.choose_flexi_password_type()
    if flexi_password_type == 1:
        FlexiPassword.all_shuffled_same_sc_num(no_of_passwords,  base_word , sc_amount,
                                               num_amount)
    elif flexi_password_type == 2:
        FlexiPassword.all_shuffled_diff_sc_num(no_of_passwords,  base_word , sc_amount,
                                               num_amount)
    elif flexi_password_type == 3:
        FlexiPassword.all_shuffled_diff_sc_same_num(no_of_passwords,  base_word, sc_amount,
                                                    num_amount)
    elif flexi_password_type == 4:
        FlexiPassword.all_shuffled_same_sc_diff_num(no_of_passwords, base_word , sc_amount,
                                                    num_amount)
    elif flexi_password_type == 5:
        FlexiPassword.base_word_not_shuffled_same_sc_num(no_of_passwords,  base_word , sc_amount,
                                                         num_amount)
    elif flexi_password_type == 6:
        FlexiPassword.base_word_not_shuffled_diff_sc_num(no_of_passwords,  base_word , sc_amount,
                                                         num_amount)


elif user_choice == "3":
    no_of_passwords = FlexiPassword.number_of_passwords_generated()
    lowercase_base_word_without_spaces, length_of_base_word = FlexiPassword.input_base_word()
    #num_capital_letters = FlexiPassword.capital_characters()
    sc_amount, num_amount = FlexiPassword.number_of_special_characters_and_numbers(length_of_base_word)
    flexi_password_type = FlexiPassword.choose_flexi_password_type()
    if flexi_password_type == 1:
       FlexiPassword.all_shuffled_same_sc_num(no_of_passwords, lowercase_base_word_without_spaces,  sc_amount, num_amount)
    elif flexi_password_type == 2:
        FlexiPassword.all_shuffled_diff_sc_num(no_of_passwords, lowercase_base_word_without_spaces, sc_amount,
                                               num_amount)
    elif flexi_password_type == 3:
        FlexiPassword.all_shuffled_diff_sc_same_num(no_of_passwords, lowercase_base_word_without_spaces, sc_amount,
                                               num_amount)
    elif flexi_password_type == 4:
        FlexiPassword.all_shuffled_same_sc_diff_num(no_of_passwords, lowercase_base_word_without_spaces, sc_amount,
                                               num_amount)
    elif flexi_password_type == 5:
        FlexiPassword.base_word_not_shuffled_same_sc_num(no_of_passwords, lowercase_base_word_without_spaces, sc_amount,
                                               num_amount)
    elif flexi_password_type == 6:
        FlexiPassword.base_word_not_shuffled_diff_sc_num(no_of_passwords, lowercase_base_word_without_spaces, sc_amount,
                                               num_amount)









