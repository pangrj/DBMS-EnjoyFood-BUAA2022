import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from ChoseMenu.models import ChoseMenu
from Dish.models import Dish
from student.models import Student


# Create your views here.

def choose(request):
    if request.method == "POST":

        print(12)
        data = json.loads(request.body)
        s_id = data.get('s_id')
        d_id = data.get('d_id')
        ret = {}

        student_list = Student.objects.filter(s_id__exact=s_id)
        if len(student_list) == 0:
            ret = {"success": False, "message": "No Such Student"}
        else:
            dish_list = Dish.objects.filter(d_id=d_id)
            if len(dish_list) == 0:
                ret = {"success": False, "message": "No Such Dish"}
            else:
                if len(ChoseMenu.objects.filter(s_id__exact=s_id, d_id__exact=d_id)) != 0:
                    ret = {"success": False, "message": "Already Choose"}
                else:
                    ChoseMenu.objects.create(s_id=s_id, d_id=d_id)
                    dishes = Dish.objects.exclude(
                        d_id__in=ChoseMenu.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True))
                    retDishes = serializers.serialize('json', list(dishes))
                    ret = {"success": True, "message": "Choose success!", "dishes": retDishes}
        return JsonResponse(ret)
    else:
        return render(request, "choose.html", context={'success': True, 'message': "success"})


def delete_dish(request):
    if request.method == "POST":
        data = json.loads(request.body)
        s_id = data.get('s_id')
        d_id = data.get('d_id')
        ret = {}

        student_list = Student.objects.filter(s_id__exact=s_id)
        if len(student_list) == 0:
            ret = {"success": False, "message": "No Such Student"}
        else:
            dish_list = Dish.objects.filter(d_id=d_id)
            if len(dish_list) == 0:
                ret = {"success": False, "message": "No Such Dish"}
            else:
                chosen_unit = ChoseMenu.objects.filter(s_id__exact=s_id, d_id__exact=d_id)
                if len(chosen_unit) == 0:
                    ret = {"success": False, "message": "No Such Choose"}
                else:
                    chosen_unit.delete()
                    dishes = Dish.objects.exclude(
                        d_id__in=ChoseMenu.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True))
                    ret_dishes = serializers.serialize('json', list(dishes))
                    ret = {"success": True, "message": "Delete Success!", "dishes": ret_dishes}
        return JsonResponse(ret)
    else:
        ret = {"success": False, "message": "Delete Error!"}
        return JsonResponse(ret)


def show_select_dishes(request):
    if request.method == "POST":
        data = json.loads(request.body)
        s_id = data.get('s_id')
        ret = {}
        student_list = Student.objects.filter(s_id__exact=s_id)
        if len(student_list) == 0:
            ret = {"success": False, "message": "No Such Student"}
        else:
            dishes = Dish.objects.filter(
                d_id__in=ChoseMenu.objects.filter(s_id__exact=s_id).values_list('d_id', flat=True))
            ret_dishes = serializers.serialize('json', list(dishes))
            ret = {"success": True, "message": "Get Selected Dishes Success!", "dishes": ret_dishes}
        return JsonResponse(ret)
    else:
        ret = {"success": False, "message": "Show Error!"}
        return JsonResponse(ret)
