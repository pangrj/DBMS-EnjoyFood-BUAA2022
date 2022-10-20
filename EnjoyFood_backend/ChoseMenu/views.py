import json

from django.shortcuts import render


# Create your views here.

def choose(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ret = {"success": True, "message": "Chose Success!", "dishes": {}}
        return ret
    else:
        return render(request, "choose.html", context={'success': True, 'message': "success"})
