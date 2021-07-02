from django.shortcuts import render

from .models import Topshiriq


def index(request):
    topshiriqlar = Topshiriq.objects.all()
    context = {
        'topshiriqlar': topshiriqlar
    }
    return render(request, 'dashboard/index.html', context)
