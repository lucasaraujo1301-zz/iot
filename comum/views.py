from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from comum.models import *
from datetime import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder


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


def speed_droid_script(request, speed):
    data = {}

    time = datetime.now().strftime("%H:%M:%S")

    velocity = Speed.objects.filter(speed=speed, time=time).first()

    if not velocity:
        Speed.objects.create(speed=speed, time=time)

    return JsonResponse(data, safe=False)


def speed(request):
    speeds = Speed.objects.all()

    times = [speed.time.strftime('%H:%M') for speed in speeds]
    speeds = [speed.speed for speed in speeds]

    context = {
        'times': json.dumps(times, cls=DjangoJSONEncoder),
        'speeds': json.dumps(speeds),
    }

    return render(request, 'comum/alarm.html', locals())
