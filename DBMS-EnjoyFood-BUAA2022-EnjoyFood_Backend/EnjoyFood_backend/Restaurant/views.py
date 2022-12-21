import json

from django.core import serializers
from django.http import JsonResponse

from Restaurant.models import Restaurant
from util import RET


# Create your views here.
def get_restaurant_info(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)

        re_id = data.get('re_id')

        restaurant_list = Restaurant.objects.filter(id=re_id)

        if len(restaurant_list) == 1:
            ret_dishes = json.loads(serializers.serialize('json', list(restaurant_list)))
            ret.set_code(200)
            ret.set_message('Find Such Restaurant!')
            ret.load_data({'re_info': ret_dishes})
        else:
            ret.set_code(400)
            ret.set_message('Did not Find Such Restaurant!')
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())
