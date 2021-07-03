from django.shortcuts import render


def login(request):
    return render(request, 'user/login.html')

def profile(request):
    return render(request, 'user/profile.html')