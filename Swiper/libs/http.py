from django.http import JsonResponse

from common import errors


def render_json(code=errors.ok,data=None):
    '''
    :param code: 状态码
    :param data: 接口数据
    :return: json格式
    '''
    result = {
        'code':code
    }
    if data:
        result['data'] = data
    return JsonResponse(data=result,json_dumps_params={'separators':(",",':')})