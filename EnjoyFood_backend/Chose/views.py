import json

from django.core import serializers
from django.http import JsonResponse

from Chose.models import Chose
from Dish.models import Dish
from User.models import User
from util import RET


# Create your views here.

def choose(request):
    ret = RET.get_instance()
    if request.method == "POST":
        data = json.loads(request.body)
        s_id = data.get('s_id')
        d_id = data.get('d_id')
        # ret = {}

        student_list = User.objects.filter(s_id__exact=s_id)
        if len(student_list) == 0:
            ret.code = 400
            ret.message = 'No Such Student'
            # ret = {"success": False, "message": "No Such Student"}
        else:
            dish_list = Dish.objects.filter(d_id=d_id)
            if len(dish_list) == 0:
                ret.code = 401
                ret.message = 'No Such Dish'
                # ret = {"success": False, "message": "No Such Dish"}
            else:
                if len(Chose.objects.filter(s_id__exact=s_id, d_id__exact=d_id)) != 0:
                    ret.code = 402
                    ret.message = 'Already Choose'
                    # ret = {"success": False, "message": "Already Choose"}
                else:
                    Chose.objects.create(s_id=s_id, d_id=d_id)
                    dishes = Dish.objects.exclude(
                        d_id__in=Chose.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True))
                    retDishes = serializers.serialize('json', list(dishes))

                    ret.code = 200
                    ret.message = 'Choose success!'
                    ret.data = {"dishes": retDishes}

                    # ret = {"success": True, "message": "Choose success!", "dishes": retDishes}
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def delete_dish(request):
    ret = RET.get_instance()
    if request.method == "POST":
        data = json.loads(request.body)
        s_id = data.get('s_id')
        d_id = data.get('d_id')

        student_list = User.objects.filter(s_id__exact=s_id)
        if len(student_list) == 0:
            ret.code = 400
            ret.message = 'No Such Student'
            # ret = {"success": False, "message": "No Such Student"}
        else:
            dish_list = Dish.objects.filter(d_id=d_id)
            if len(dish_list) == 0:
                ret.code = 401
                ret.message = 'No Such Dish'
                # ret = {"success": False, "message": "No Such Dish"}
            else:
                chosen_unit = Chose.objects.filter(s_id__exact=s_id, d_id__exact=d_id)
                if len(chosen_unit) == 0:
                    ret.code = 402
                    ret.message = 'No Such Choose'
                    # ret = {"success": False, "message": "No Such Choose"}
                else:
                    chosen_unit.delete()
                    dishes = Dish.objects.exclude(
                        d_id__in=Chose.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True))
                    ret_dishes = serializers.serialize('json', list(dishes))
                    ret.code = 200
                    ret.message = 'Delete Success!'
                    ret.data = {"dishes": ret_dishes}
                    # ret = {"success": True, "message": "Delete Success!", "dishes": ret_dishes}
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def show_select_dishes(request):
    ret = RET.get_instance()
    if request.method == "POST":
        data = json.loads(request.body)
        s_id = data.get('s_id')
        student_list = User.objects.filter(s_id__exact=s_id)
        if len(student_list) == 0:
            ret.code = 400
            ret.message = 'No Such Student'
            # ret = {"success": False, "message": "No Such Student"}
        else:
            dishes = Dish.objects.filter(
                d_id__in=Chose.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True))
            ret_dishes = serializers.serialize('json', list(dishes))
            ret.code = 200
            ret.message = 'Get Selected Dishes Success!'
            ret.data = {"dishes": ret_dishes}
            # ret = {"success": True, "message": "Get Selected Dishes Success!", "dishes": ret_dishes}
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        # ret = {"success": False, "message": "Show Error!"}
        return JsonResponse(ret.json_type())
