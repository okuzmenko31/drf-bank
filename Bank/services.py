import random


def create_card():
    first_part = '5168'
    sec_part = ''.join([str(random.randint(1, 9)) for x in range(12)])
    card = first_part + sec_part
    return card
