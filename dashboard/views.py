from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Topshiriq


@login_required
def index(request):
    topshiriqlar = Topshiriq.objects.all()
    context = {
        'topshiriqlar': topshiriqlar
    }
    return render(request, 'dashboard/index.html', context)
