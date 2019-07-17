import random
import re

PHONE_PATTERN = re.compile(r'^1[3-9]\d{9}$')

def is_phoneNum(phone_num):
    return True if PHONE_PATTERN.match(phone_num.strip()) else False


def gen_randomCode(length=4):
    if not isinstance(length,int):
        length = 1

    elif length <= 1:
        length = 1
    return str(random.randrange(10**(length-1),10**length))