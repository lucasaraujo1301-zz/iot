from django.urls import path

from comum.views import *


urlpatterns = [
    path('', index, name='index'),
    path('change/lamp/<int:id>/<str:on>', change_lamp, name='change_lamp'),
    path('teste/droidscript/<int:x>/<int:y>', teste_droid, name='teste_droid')
]
