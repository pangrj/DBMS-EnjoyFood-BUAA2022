import json

from django.http import JsonResponse
from django.shortcuts import *

from student.models import Student


# Create your views here.
def home(request):
    username = ''
    message = ''
    return render(request, 'login.html', context={'success': True, 'username': username, 'message': message})


def register(request):
    if request.method == 'POST':
        new_s_id = request.POST.get('s_id')
        new_s_password = request.POST.get('s_password')
        new_student = Student(s_id=new_s_id, s_password=new_s_password)
    else:
        return render(request, context={'success': False, 'message': "register method error"})


def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_s_id = data.get('s_id')
        new_s_password = data.get('s_password')
        new_student = Student(s_id=new_s_id, s_password=new_s_password)
        new_student.save()
        ret = {'success': True, 'message': "register success"}
        return JsonResponse(ret)
    else:
        ret = {'success': True, 'message': "register success"}
        return JsonResponse(ret)
