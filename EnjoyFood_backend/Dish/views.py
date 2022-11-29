import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from Dish.models import *

from Chose.models import *
from student.models import *


# Create your views here.
def showNotSelectMenu(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        s_id = data.get('s_id')

        # 找到此学生未选过的菜品
        dishes = Dish.objects.exclude(
            d_id__in=Chose.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True))
        retDishes = serializers.serialize('json', list(dishes))
        ret = {'success': True, 'message': "Show success", 'dishes': retDishes}

        return JsonResponse(ret)
    else:
        ret = {'success': False, 'message': "menu initial error"}
        return JsonResponse(ret)


def initial(request):
    if request.method == 'POST':
        Dish.objects.create(d_name='卤肉饭', d_category='套饭', d_cuisine='粤菜', d_calories=413, d_price=12)
        Dish.objects.create(d_name='宫爆鸡丁', d_category='荤菜', d_cuisine='川菜', d_calories=213, d_price=8)
        Dish.objects.create(d_name='烤冷面', d_category='小食', d_cuisine='东北菜', d_calories=160, d_price=8)
        Dish.objects.create(d_name='麻婆豆腐', d_category='素菜', d_cuisine='川菜', d_calories=100, d_price=5)
        Dish.objects.create(d_name='冬阴功汤', d_category='汤菜', d_cuisine='泰式', d_calories=200, d_price=10)
        ret = {'success': True, 'message': "Initial success"}
        return JsonResponse(ret)
    else:
        ret = {'success': False, 'message': "menu initial error"}
        return JsonResponse(ret)


def searchByName(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        d_name = data.get("d_name")
        s_id = data.get('s_id')
        if len(Student.objects.filter(s_id=s_id)) == 0:
            ret = {'success': False, 'message': "Enter right student_id!"}
            return JsonResponse(ret)
        dishes = Dish.objects.exclude(
            d_id__in=Chose.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True)).filter(d_name=d_name)
        # dishes = Dish.objects.filter(d_name=d_name)
        retDishes = serializers.serialize('json', list(dishes))
        if len(dishes) == 0:
            ret = {'success': False, 'message': "No Such Dishes Not Selected!"}
        else:
            ret = {'success': True, 'message': "Find Dishes!", 'dishes': retDishes}
        return JsonResponse(ret)
    else:
        ret = {'success': False, 'message': "Error HTTP Method!"}
        return JsonResponse(ret)
