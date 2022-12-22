import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from ExerArea.models import ExerArea
from util import RET


# Create your views here.
def get_exer_area_info(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)

        l_id = data.get('l_id')

        exer_area_list = ExerArea.objects.filter(id=l_id)

        if len(exer_area_list) == 1:
            ret_area = json.loads(serializers.serialize('json', list(exer_area_list)))
            ret.set_code(200)
            ret.set_message('Find Such Exercise Area!')
            ret.load_data({'re_info': ret_area})
        else:
            ret.set_code(400)
            ret.set_message('Did not Find Such Exercise Area!')
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())
