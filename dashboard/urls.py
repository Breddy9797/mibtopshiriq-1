"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from dashboard import views as dash_views

urlpatterns = [
                  path('', dash_views.index, name='dash-index'),
                  path('add/', dash_views.add_task, name='add-task'),
                  path('detail/<int:pk>', dash_views.detail, name='dash-detail'),
                  path('update/<int:pk>', dash_views.update, name='dash-update'),
                  path('delete/<int:pk>', dash_views.delete, name='dash-delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
