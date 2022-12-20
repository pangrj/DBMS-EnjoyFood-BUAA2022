import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from Dish.models import *

from Chose.models import *
from User.models import *
from util import RET


# Create your views here.

def showDishMenu(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)

        u_name = data.get('u_name')

        dishes = Dish.objects.all()
        retDishes = serializers.serialize('json', list(dishes))

        ret.code = 200
        ret.message = "Show Success!"
        ret.load_data({'dishes': retDishes})
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def showNotSelectMenu(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        s_id = data.get('s_id')

        # 找到此学生未选过的菜品
        dishes = Dish.objects.exclude(
            d_id__in=Chose.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True))
        retDishes = serializers.serialize('json', list(dishes))

        ret.code = 200
        ret.message = "Show Success!"
        ret.data = {'dishes': retDishes}
        # ret = {'success': True, 'message': "Show success", 'dishes': retDishes}

        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def initial(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        Dish.objects.create(d_name='卤肉饭', d_category='套饭', d_cuisine='粤菜', d_calories=413, d_price=12)
        Dish.objects.create(d_name='宫爆鸡丁', d_category='荤菜', d_cuisine='川菜', d_calories=213, d_price=8)
        Dish.objects.create(d_name='烤冷面', d_category='小食', d_cuisine='东北菜', d_calories=160, d_price=8)
        Dish.objects.create(d_name='麻婆豆腐', d_category='素菜', d_cuisine='川菜', d_calories=100, d_price=5)
        Dish.objects.create(d_name='冬阴功汤', d_category='汤菜', d_cuisine='泰式', d_calories=200, d_price=10)
        ret.code = 200
        ret.message = 'Initial success'
        # ret = {'success': True, 'message': "Initial success"}
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def searchByName(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        d_name = data.get("d_name")
        s_id = data.get('s_id')
        if len(User.objects.filter(s_id=s_id)) == 0:
            ret.code = 400
            ret.message = 'Enter right student_id!'
            # ret = {'success': False, 'message': "Enter right student_id!"}
            return JsonResponse(ret.json_type())
        dishes = Dish.objects.exclude(
            d_id__in=Chose.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True)).filter(d_name=d_name)
        # dishes = Dish.objects.filter(d_name=d_name)
        retDishes = serializers.serialize('json', list(dishes))
        if len(dishes) == 0:
            ret.code = 401
            ret.message = 'No Such Dishes Not Selected!'
            # ret = {'success': False, 'message': "No Such Dishes Not Selected!"}
        else:
            ret.code = 200
            ret.message = 'Find Dishes!'
            ret.data = {'dishes': retDishes}
            # ret = {'success': True, 'message': "Find Dishes!", 'dishes': retDishes}
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        # ret = {'success': False, 'message': "Error HTTP Method!"}
        return JsonResponse(ret.json_type())
