import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


result1 = get_random_string(10)
result2 = get_random_string(6)
result3 = get_random_string(4)

print(result1)
