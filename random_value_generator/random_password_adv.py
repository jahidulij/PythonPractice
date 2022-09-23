import random
import string


def get_password(up_case_length, low_case_length, digits_length, special_char_length, total_length):
    random_loop_length = total_length - up_case_length - low_case_length - digits_length - special_char_length

    password = ''
    punc = '@#$&*!'

    for i in range(up_case_length):
        password += random.choice(string.ascii_uppercase)

    for i in range(low_case_length):
        password += random.choice(string.ascii_lowercase)

    for i in range(digits_length):
        password += random.choice(string.digits)

    for i in range(random_loop_length):
        password += random.choice(string.ascii_letters)

    for i in range(special_char_length):
        password += random.choice(punc)

    password_list = list(password)
    password = ''.join(password_list)
    # print(password)
    # password = password.replace('a', '_')
    return password


up_case = 1
low_case = 7
digits = 1
special_char = 1
min_length = 10

result2 = get_password(up_case, low_case, digits, special_char, min_length)

print(result2)
