from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Topshiriq
from .forms import TopshiriqForm


@login_required
def index(request):
    topshiriqlar = Topshiriq.objects.all()
    context = {
        'topshiriqlar': topshiriqlar,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TopshiriqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash-index')
    else:
        form = TopshiriqForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_task.html', context)


def detail(request, pk):
    task = Topshiriq.objects.get(id=pk)
    context = {
        'task': task,
    }
    return render(request, 'dashboard/detail.html', context)
