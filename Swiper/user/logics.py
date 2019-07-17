from django.core.cache import cache

from common import cache_keys
from common.utils import gen_randomCode
from libs.sms import send_verify_code


def send_verifyCode(phone_num):
    code = gen_randomCode(5)
    ret = send_verify_code(phone_num,code)
    if ret:
        cache.set(cache_keys.VERIFY_CODE_CACHE_PREFIX.format(phone_num),code,60*3)
    return ret