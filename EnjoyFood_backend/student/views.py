import json

from django.http import JsonResponse
from django.shortcuts import *

from student.models import Student
from util import RET


# Create your views here.
def home(request):
    username = ''
    message = ''
    return render(request, 'login.html', context={'success': True, 'username': username, 'message': message})


def Hello(request):
    ret = RET.get_instance()
    if request.method == 'POST':

        ret.code = 200
        ret.message = 'Hello!'
        ret_text = ret.json_type()
        return JsonResponse(ret_text)
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_s_id = data.get('s_id')
        new_s_password = data.get('s_password')

        student_list = Student.objects.filter(s_id__exact=new_s_id)

        if len(student_list) == 0:
            new_student = Student(s_id=new_s_id, s_password=new_s_password)
            new_student.save()
            ret = {'success': True, 'message': "register success"}
        else:
            ret = {'success': False, 'message': "The user has been registered!"}
    else:
        return render(request, context={'success': False, 'message': "register method error"})


def login(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        new_s_id = data.get('s_id')
        new_s_password = data.get('s_password')
        student_list = Student.objects.filter(s_id__exact=new_s_id)
        if len(student_list) == 1:
            student = student_list[0]
            if new_s_password == student.s_password:
                ret.code = 200
                ret.message = "login success"
            else:
                ret.code = 400
                ret.message = "password error"
        else:
            new_student = Student(s_id=new_s_id, s_password=new_s_password)
            new_student.save()

            ret.code = 201
            ret.message = "register success"
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def modify_infor(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        s_id = data.get('s_id')
        s_password = data.get('s_password')
        s_name = data.get('s_name')
        s_dorm = data.get('s_dorm')
        s_gender = data.get('s_gender')
        student_list = Student.objects.filter(s_id__exact=s_id)
        if len(student_list) == 0:
            ret.code = 400
            ret.message = "Did not Find the Student!"
        else:
            student = student_list[0]
            if len(s_password) == 0:
                ret.code = 401
                ret.message = "Please Enter A correct Password!"
                # ret = {'success': False, 'message': "Please Enter A correct Password!"}
            else:
                student.s_password = s_password
                student.s_name = s_name
                student.s_dorm = s_dorm
                student.s_gender = s_gender
                student.save()
                ret.code = 200
                ret.message = "Modify Success!"
                # ret = {'success': True, 'message': "Modify Success!"}
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        # ret = {'success': False, 'message': "HTTP Method Error!"}
        return JsonResponse(ret.json_type())
