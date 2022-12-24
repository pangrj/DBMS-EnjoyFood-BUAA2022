import json

from django.core import serializers
from django.http import JsonResponse

from Plan.models import *
from User.models import User
from util import RET
from util.RET import get_time


# Create your views here.
def get_plan_by_u_name(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        u_name = data.get('u_name')

        user_list = User.objects.filter(u_name=u_name)

        if len(user_list) == 1:
            user = user_list[0]
            plan_list = Plan.objects.filter(user_id=user.get_u_id())
            ret_plans = json.loads(serializers.serialize('json', list(plan_list)))

            for plan in ret_plans:
                plan['fields']['p_time'] = get_time(plan.get('fields').get('p_time'))

            ret.code = 200
            ret.message = "Get Plan Success!"
            ret.load_data({'p_Array': ret_plans})
            ret.load_data({'num': len(plan_list)})
        else:
            ret.set_code(400)
            ret.set_message('No Such Student')
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def get_plan_details(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        p_id = data.get('p_id')

        plan_list = Plan.objects.filter(id=p_id)

        if len(plan_list) == 0:
            ret.set_code(400)
            ret.set_message('No Such Plan!')
        else:
            ret_plans = json.loads(serializers.serialize('json', list(plan_list)))

            for plan in ret_plans:
                plan['fields']['p_time'] = get_time(plan.get('fields').get('p_time'))

            dishes = Dish.objects.filter(d_id__in=PlanOfDish.objects.filter(plan_id=p_id).values_list('dish_id'))
            ret_dishes = json.loads(serializers.serialize('json', list(dishes)))

            exercises = Exercise.objects.filter(planofexercise__plan_id=p_id)
            ret_exercise = json.loads(serializers.serialize('json', list(exercises)))

            ret.code = 200
            ret.message = "Show Success!"
            ret.load_data({'dishes': ret_dishes})
            ret.load_data({'exercises': ret_exercise})
            ret.load_data({'plan': ret_plans})
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def add_plan(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        u_name = data.get('u_name')
        user_list = User.objects.filter(u_name=u_name)

        if len(user_list) == 1:
            user = user_list[0]
            d_id_list = data.get('d_id')
            sp_id_list = data.get('sp_id')
            p_name = data.get('p_name')
            p_description = data.get('p_description')
            plan = Plan(p_name=p_name, p_description=p_description, user_id=user.get_u_id())
            plan.save()
            calories_in = 0
            calories_consume = 0
            for d_id in d_id_list:
                calories_in += Dish.objects.get(d_id=d_id).d_calories
                plan_of_dish = PlanOfDish(plan_id=plan.get_p_id(), dish_id=d_id)
                plan_of_dish.save()
            for sp_id in sp_id_list:
                calories_consume += Exercise.objects.get(id=sp_id).sp_calories
                plan_of_exercise = PlanOfExercise(plan_id=plan.get_p_id(), exercise_id=sp_id)
                plan_of_exercise.save()
            plan.calories_in = calories_in
            plan.calories_consume = calories_consume
            plan.save()
            ret.code = 200
            ret.message = "Add Plan Success!"
        else:
            ret.set_code(400)
            ret.set_message('No Such Student')
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def get_latest_plan_calories(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)

        u_name = data.get('u_name')

        plan_list = Plan.objects.filter(user__u_name=u_name).order_by('-pk', 'p_time')
        calories_in = []
        calories_minus = []
        time = []
        inClas = 0
        outClas = 0
        num = 0
        for plan in plan_list:
            num += 1
            calories_in.append(plan.calories_in)
            inClas += plan.calories_in
            outClas += plan.calories_consume
            calories_minus.append((plan.calories_in - plan.calories_consume))
            time.append(get_time(str(plan.p_time)))

        ret.set_code(200)
        ret.set_message('get calories success')
        ret.load_data({'num': num})
        ret.load_data({'time': time})
        ret.load_data({'cals_in_list': calories_in})
        ret.load_data({'cals_minus_list': calories_minus})

        ret.load_data({'inClas': inClas})
        ret.load_data({'outClas': outClas})
        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())


def delete_plan(request):
    ret = RET.get_instance()
    if request.method == 'POST':
        data = json.loads(request.body)
        plan_id = data.get('plan_id')

        plan_list = Plan.objects.filter(id=plan_id)

        if len(plan_list) == 0:
            ret.set_code(400)
            ret.set_message('No Such Plan!')
        else:
            plan = plan_list[0]
            plan.delete()

            ret.set_code(200)
            ret.set_message('Plan Delete Success!')

        return JsonResponse(ret.json_type())
    else:
        ret.Http_error()
        return JsonResponse(ret.json_type())
