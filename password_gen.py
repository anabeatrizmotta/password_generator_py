import random
import string
    
def password_generator(lenght_pw = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options


    pw_user = ''

    for i in range(0, lenght_pw):
        digit = random.choice(options)
        pw_user = pw_user + digit

    return pw_user
    
choice_user = input("Password length: ")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Invalid input")
    quit()

response = password_generator(lenght_pw = choice_user)
print(f"New password generated:\n{response}")




