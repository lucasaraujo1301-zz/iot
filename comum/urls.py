from django.urls import path

from comum.views import *


urlpatterns = [
    path('', index, name='index'),
    path('change/lamp/<int:id>/<str:on>', change_lamp, name='change_lamp'),
    path('alarm/droidscript/<int:x>/<int:y>', alarm_droid_script, name='alarm_droid_script'),
    path('alarm/', alarm, name='alarm'),
]
