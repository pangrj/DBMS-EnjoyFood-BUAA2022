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
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())
