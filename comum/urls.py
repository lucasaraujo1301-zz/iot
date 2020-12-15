from django.urls import path

from comum.views import *


urlpatterns = [
    path('', index, name='index'),
    path('change/lamp/<int:id>/<str:on>', change_lamp, name='change_lamp'),
    path('speed/droidscript/<int:speed>/', speed_droid_script, name='speed_droid_script'),
    path('speed/', speed, name='speed'),
]
