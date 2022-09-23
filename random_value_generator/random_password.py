import random
import string


def get_random_password(length):

    password = random.choice(string.ascii_uppercase)
    # select 1 lowercase
    password += random.choice(string.ascii_lowercase)


    punc = string.punctuation
    # generate other characters
    for i in range(length-4):
        password += random.choice(string.ascii_letters)

    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice(punc)

    password_list = list(password)
    # shuffle all characters
    # random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


print("First Random Password is ", get_random_password(8))
