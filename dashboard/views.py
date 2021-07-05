from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Topshiriq
from .forms import TopshiriqForm


@login_required
def index(request):
    topshiriqlar = Topshiriq.objects.all()
    hodimlar = User.objects.all()
    admin_soni = Topshiriq.objects.filter(ijrochi=1).count()
    alisher_soni = Topshiriq.objects.filter(ijrochi=2).count()
    om_soni = Topshiriq.objects.filter(prioritet='O\'ta muhim').count()
    m_soni = Topshiriq.objects.filter(prioritet='Muhim').count()
    o_soni = Topshiriq.objects.filter(prioritet='Oddiy').count()
    ariza = Topshiriq.objects.filter(topshiriq_turi='Ariza').count()
    murojat = Topshiriq.objects.filter(topshiriq_turi='Murojat').count()
    taklif = Topshiriq.objects.filter(topshiriq_turi='Taklif').count()
    aloqa_xati = Topshiriq.objects.filter(topshiriq_turi='Aloqa xati').count()
    topshiriq = Topshiriq.objects.filter(topshiriq_turi='Topshiriq').count()

    context = {
        'topshiriqlar': topshiriqlar,
        'om_soni': om_soni,
        'm_soni': m_soni,
        'o_soni': o_soni,
        'hodimlar': hodimlar,
        'admin_soni': admin_soni,
        'alisher_soni': alisher_soni,
        'ariza': ariza,
        'murojat': murojat,
        'taklif': taklif,
        'aloqa_xati': aloqa_xati,
        'topshiriq': topshiriq,
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
