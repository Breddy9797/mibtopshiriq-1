from django.contrib import messages
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
        form = TopshiriqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            topshiriq_raqami = form.cleaned_data.get('topshiriq_raqami')
            messages.success(request, f'{topshiriq_raqami} raqamli topshiriq yaratildi')
            return redirect('dash-index')
    else:
        form = TopshiriqForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_task.html', context)


@login_required
def detail(request, pk):
    task = Topshiriq.objects.get(id=pk)
    context = {
        'task': task,
    }
    return render(request, 'dashboard/detail.html', context)


@login_required
def update(request, pk):
    task = Topshiriq.objects.get(id=pk)
    if request.method == 'POST':
        form = TopshiriqForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            topshiriq_raqami = form.cleaned_data.get('topshiriq_raqami')
            messages.success(request, f'{topshiriq_raqami} raqamli topshiriq muvofaqiyatli o\'zgardi')
            return redirect('dash-index')
    else:
        form = TopshiriqForm(instance=task)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/update.html', context)


def delete(request, pk):
    task = Topshiriq.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, ' Topshiriq o\'chirildi!')
        return redirect('dash-index')
    return render(request, 'dashboard/delete.html')
