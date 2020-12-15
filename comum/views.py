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


def alarm_droid_script(request, x, y):
    data = {}

    position = str(x)+','+str(y)
    time = datetime.now().strftime("%H:%M")

    alarm = Alarm.objects.filter(position=position, time=time).first()

    if not alarm:
        Alarm.objects.create(position=position, time=time)

    return JsonResponse(data, safe=False)


def alarm(request):
    alarms = Alarm.objects.all()

    times = [alarm.time.strftime('%H:%M') for alarm in alarms]
    positionsy = [alarm.position.split(',')[1] for alarm in alarms]
    positionsx = [alarm.position.split(',')[0] for alarm in alarms]

    context = {
        'times': json.dumps(times, cls=DjangoJSONEncoder),
        'positionsy': json.dumps(positionsy),
        'positionsx': json.dumps(positionsx)
    }

    return render(request, 'comum/alarm.html', locals())
