from django.urls import path

from comum.views import *


urlpatterns = [
    path('', index, name='index'),
]