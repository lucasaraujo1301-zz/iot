from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from authentication.forms import *
from authentication.helpers import *
from django.contrib.auth.hashers import make_password


def application_login(request):
    form = AuthenticationForm(request)

    if request.POST:
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())

            if "next" in request.GET:
                return HttpResponseRedirect(request.GET.get("next"))
            else:
                return HttpResponseRedirect(reverse('comum:index'))
        else:
            messages.warning(request, "Username/Password are wrong or your user are inactive")

    return render(request, 'authenticate/login.html', locals())


def application_logout(request):
    logout(request)

    messages.success(request, "You make log out from the system!")
    return HttpResponseRedirect(reverse('comum:index'))


def register(request):
    form = NewUserForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            cpf_unmask = CPF.get_digits(form.cleaned_data.get('cpf'))
            user = User.objects.create(username=cpf_unmask,
                                       password=make_password(form.cleaned_data.get("password1")),
                                       email=form.cleaned_data.get("email"))
            usuario = form.save(commit=False)
            usuario.user = user
            usuario.save()

            messages.success(request, "Registration completed. Log in to continue.")
            return HttpResponseRedirect(
                reverse(
                    'authentication:application_login') + "?next=%s" % request.GET.get("next", "/")
            )

    return render(request, 'authenticate/register.html', locals())

