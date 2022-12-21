import json
import os

from django.http import JsonResponse

from EnjoyFood_backend.settings import MEDIA_ROOT
from User.models import User
from util import RET


# Create your views here.

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
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)

        new_u_name = data.get('u_name')
        new_u_password = data.get('u_password')

        user_list = User.objects.filter(u_name__exact=new_u_name)
        if len(user_list) == 0:
            new_user = User(u_name=new_u_name, u_password=new_u_password)
            new_user.save()
            ret.set_code(200)
            ret.set_message('register success')
        else:
            ret.set_code(400)
            ret.set_message('Username Already contains!')
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def login(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        new_u_name = data.get('u_name')
        new_u_password = data.get('u_password')
        user_list = User.objects.filter(u_name=new_u_name)
        if len(user_list) == 1:
            user = user_list[0]
            if new_u_password == user.get_u_password():
                ret.set_code(200)
                ret.set_message('login success')
            else:
                ret.set_code(400)
                ret.set_message('password error')
        else:
            ret.set_code(401)
            ret.set_message('no such user!')
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def modify_infor(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        u_avatar = request.FILES.get('u_avatar')
        # avatar_name = request.POST.get('avatar_name')
        data = request.POST
        u_name = data.get('u_name')
        print(u_name)
        u_password = data.get('u_password')
        print(u_password)
        u_height = data.get('u_height')
        print(u_height)
        u_weight = data.get('u_weight')
        print(u_weight)
        u_age = data.get('u_age')
        print(u_age)
        u_position = data.get('u_position')
        print(u_position)
        u_gender = data.get('u_gender')
        print(u_gender)
        u_email = data.get('u_email')
        print(u_email)
        # u_avatar = data.get('u_photo')
        user_list = User.objects.filter(u_name__exact=u_name)
        if len(user_list) == 0:
            ret.set_code(400)
            ret.set_message("Did not Find the User!")
        else:
            user = user_list[0]
            if len(u_password) == 0:
                ret.set_code(401)
                ret.set_message("Please Enter A correct Password!")
            else:
                user.set_u_password(u_password)
                user.set_u_position(u_position)
                user.set_u_gender(u_gender)
                user.set_u_email(u_email)
                user.set_u_avatar(u_avatar)
                user.set_u_height(u_height)
                user.set_u_weight(u_weight)
                user.u_age = u_age
                user.save()
                ret.set_code(200)
                ret.set_message("Modify Success!")
                avatar_addr = user.get_avatar_url()
                ret.load_data({'img_path': avatar_addr})
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def upLoadImg(request):
    ret = RET.get_instance()

    if request.method == 'POST':
        img = request.FILES.get('img')
        u_name = request.POST.get('u_name')
        user = User.objects.get(u_name__exact=u_name)
        user.u_avatar.delete()
        user.u_avatar = img
        user.save()
        avatar_addr = user.get_avatar_url()
        '''image_path = os.path.join(MEDIA_ROOT, img_name)
        with open(image_path, 'wb') as fp:
            # 遍历图片的块数据（切块的传图片）
            for i in img.chunks():
                # 将图片数据写入自己的那个文件
                fp.write(i)'''

        ret.set_code(200)
        ret.set_message('success')
        ret.load_data({'img_path': avatar_addr})
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def get_infor(request):
    ret = RET.get_instance()

    if request.method == 'POST':
        data = json.loads(request.body)
        u_name = data.get('u_name')
        user_list = User.objects.filter(u_name=u_name)

        if len(user_list) == 1:
            user = user_list[0]
            ret.set_code(200)
            ret.set_message('get Infor success')

            ret.load_data({'u_name': user.get_u_name()})
            ret.load_data({'u_height': user.get_u_height()})
            ret.load_data({'u_weight': user.get_u_weight()})
            ret.load_data({'u_age': user.u_age})
            ret.load_data({'u_position': user.u_position})
            ret.load_data({'u_gender': user.get_u_gender()})
            ret.load_data({'u_email': user.u_email})
            ret.load_data({'u_photo': user.get_avatar_url()})
            ret.load_data({'id': user.get_u_id()})

        else:
            ret.set_code(400)
            ret.set_message('No Such Student')
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def initial(request):
    ret = RET.get_instance()

    if request.method == 'POST':
        data = json.loads(request.body)

        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def change_password(request):
    ret = RET.get_instance()

    if request.method == 'POST':
        data = json.loads(request.body)
        u_name = data.get('u_name')
        u_password = data.get('u_password')
        u_newPassword = data.get('u_newPassword')

        user_list = User.objects.filter(u_name=u_name)

        if len(user_list) == 1:
            user = user_list[0]
            if u_password == user.get_u_password():
                user.set_u_password(u_newPassword)
                ret.set_code(200)
                ret.set_message('Change Success!')
            else:
                ret.set_code(401)
                ret.set_message('Password Error!')
        else:
            ret.set_code(400)
            ret.set_message('No Such Student!')
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def get_avatar(request):
    ret = RET.get_instance()

    if request.method == 'POST':
        data = json.loads(request.body)
        u_name = data.get('u_name')
        user_list = User.objects.filter(u_name=u_name)

        if len(user_list) == 1:
            user = user_list[0]
            ret.set_code(200)
            ret.set_message('Change Success!')
            ret.load_data({'avatar_url': user.get_avatar_url()})
        else:
            ret.set_code(400)
            ret.set_message('No Such Student!')
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())
