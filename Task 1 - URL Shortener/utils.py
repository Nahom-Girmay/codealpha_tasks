import random
import string


def generate_short_code():
  
    characters = string.ascii_letters + string.digits

    short_code = "".join(
        random.choices(characters, k=6)
  )

    return short_code 

