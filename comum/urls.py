from django.urls import path

from comum.views import *


urlpatterns = [
    path('', index, name='index'),
    path('change/lamp/<int:id>/<str:on>', change_lamp, name='change_lamp'),
]
