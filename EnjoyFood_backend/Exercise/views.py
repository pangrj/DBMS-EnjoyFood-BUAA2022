import json

from django.core import serializers
from django.http import JsonResponse

from Exercise.models import Exercise
from util import RET


# Create your views here.
def showExerciseMenu(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)

        exercises = Exercise.objects.all()
        retExercises = serializers.serialize('json', list(exercises))

        ret.code = 200
        ret.message = "Show Success!"
        ret.load_data({'sports': retExercises})
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def searchByCalorie(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        u_name = data.get('u_name')
        sp_calories = data.get('sp_calories')

        sports = Exercise.objects.filter(sp_calories__gte=sp_calories)
        retSports = serializers.serialize('json', list(sports))

        ret.code = 200
        ret.message = 'Find Exercise!'
        ret.load_data({'sports': retSports})
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def searchByCircle(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        u_name = data.get('u_name')
        c_name = data.get('c_name')

        sports = Exercise.objects.filter(exerArea__lifeCircle__c_name=c_name)
        retSports = serializers.serialize('json', list(sports))

        ret.code = 200
        ret.message = 'Find Exercise!'
        ret.load_data({'sports': retSports})
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def searchByDifficulty(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        u_name = data.get('u_name')
        sp_difficulty = data.get('sp_difficulty')

        sports = Exercise.objects.filter(sp_difficulty=sp_difficulty)
        retSports = serializers.serialize('json', list(sports))

        ret.code = 200
        ret.message = 'Find Exercise!'
        ret.load_data({'sports': retSports})
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())
