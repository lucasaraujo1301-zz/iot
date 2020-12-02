from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from comum.models import *


@login_required
def index(request):
    lamps = Lamp.objects.all()
    for lamp in lamps:
        user_lamp = UserLamp.objects.filter(user=request.user, lamp=lamp).first()

        if user_lamp:
            continue
        else:
            UserLamp.objects.create(user=request.user, lamp=lamp)

    lamps = UserLamp.objects.filter(user=request.user).order_by('id')

    return render(request, 'comum/index.html', locals())


@login_required
def change_lamp(request, id, on):
    data = {}
    lamp = UserLamp.objects.filter(user=request.user, lamp_id=id).first()

    if lamp:
        lamp.active = on
        lamp.save()

        data['active'] = lamp.active
    else:
        lamp = UserLamp.objects.create(active=True, user=request.user, lamp=Lamp.objects.get(id=id))

        data['active'] = lamp.active

    return JsonResponse(data, safe=False)
