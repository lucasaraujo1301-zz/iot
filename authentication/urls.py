from django.urls import path

from authentication.views import *

urlpatterns = [
    path('login/', application_login, name='application_login'),
    path('logout/', application_logout, name='logout'),
    path('register/', register, name='register'),
]
