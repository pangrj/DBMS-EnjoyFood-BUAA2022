import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from Comment.models import CommentPlan
from Plan.models import Plan
from User.models import User
from util import RET
from util.RET import get_time


# Create your views here.
def publish_comment(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        u_name = data.get('u_name')
        p_id = data.get('p_id')
        r_star = data.get('r_star')
        r_content = data.get('r_content')
        user_list = User.objects.filter(u_name__exact=u_name)
        plan_list = Plan.objects.filter(id=p_id)
        if len(user_list) == 0:
            ret.set_code(400)
            ret.set_message("Did not Find the User!")
        else:
            user = user_list[0]
            if len(plan_list) == 0:
                ret.set_code(401)
                ret.set_message("Did not Find the Plan!")
            else:
                comment = CommentPlan.objects.create(user=user, plan=plan_list[0],
                                                     r_star=r_star, r_content=r_content)
                ret.set_code(200)
                ret.set_message("Make A Comment!")

        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def get_comment_of_Plan(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        p_id = data.get('p_id')

        plan_list = Plan.objects.filter(id=p_id)

        if len(plan_list) == 0:
            ret.set_code(400)
            ret.set_message("Did not Find the Plan!")
        else:
            comment_list = CommentPlan.objects.filter(plan_id=p_id)

            ret_comment = json.loads(serializers.serialize('json', list(comment_list)))

            for comment in ret_comment:
                id = comment.get('fields').get('user')
                u_name = User.objects.get(id=id).get_u_name()

                # get_time(comment.get('fields').get('r_data'))
                # comment = dict(comment, **{'u_name': u_name})
                comment['fields'] = dict(comment['fields'], **{'u_name': u_name})
                comment['fields']['r_data'] = get_time(comment.get('fields').get('r_data'))
            ret.set_code(200)
            ret.set_message("Make A Plan!")
            ret.load_data({'comments': ret_comment})
            return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())
