from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

from common import errors, cache_keys
from common.utils import is_phoneNum
from libs.http import render_json
from user.froms import ProfileForm
from user.logics import send_verifyCode
from user.models import User


def verify_phoneNum(request):
    '''
    校验电话号码
    生成验证码
    保存验证码
    发送验证码

    :param phone_num: 电话号码
    :return:
    '''
    phone_num = request.POST.get('phone_num')
    if is_phoneNum(phone_num):
        '''
        生成验证码
        发送验证码
        '''
        if send_verifyCode(phone_num):
            return render_json()
        else:
            return render_json(code=errors.CODE_SEND_ERR)
    else:
        return render_json(code=errors.PHONE_NUM_ERR)


def login(request):
   '''
   通过验证码登录或注册接口
   如果手机号已存在，则登录，否则，注册
   1、检测验证码是否正确
   2、注册或登录
   :param request:
   :return:
   '''
   phone_num = request.POST.get("phone_num",'')
   code = request.POST.get("code",'')
   phone_num = phone_num.strip()
   code = code.strip()

   cached_code = cache.get(cache_keys.VERIFY_CODE_CACHE_PREFIX.format(phone_num))
   if cached_code != code:
       return render_json(code=errors.VERIFY_CODE_ERR)
   user,created = User.objects.get_or_create(phonenum=phone_num)

   request.session['uid'] = user.id

   # token 认证方式
   # 为当前登录用户生成一个token。并且存储到缓存中，key为token:user.id,value为：token
   # token = user.get_or_create_token()
   # data = {'token':token}
   # return render_json(data=data)
   return render_json(data=user.to_dict())


def get_profile(request):
    user = request.user
    return render_json(data=user.profile.to_dict(exclude='auto_play'))


def set_profile(request):
    user = request.user
    form = ProfileForm(data=request.POST,instance=user.profile)
    if form.is_valid():
        form.save()
        return render_json(data=user.profile.to_dict())
    else:
        return render_json(data=form.errors)

    # uid = request.POST.get('uid')
    # try:
    #     user = User.objects.get(pk=uid)
    # except Exception as e:
    #     print(e)