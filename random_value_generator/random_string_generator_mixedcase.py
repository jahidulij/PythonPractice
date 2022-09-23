import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


result1 = get_random_string(10)

print(result1)
