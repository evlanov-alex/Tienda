from django.shortcuts import render, HttpResponse

# Create your views here.


def user_login(request):
    context = dict()
    context['can_search'] = False

    return render(request, 'login.html', context)


def user_logout(request):
    return HttpResponse('logout')


def user_register(request):
    context = dict()
    context['can_search'] = False

    return render(request, 'register.html', context)