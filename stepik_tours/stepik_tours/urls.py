"""stepik_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# – главной / – main_view ;
# – направлению /departure/<str:departure>/ – departure_view;
# – тура /tour/<int:id>/ – tour_view.

from django.contrib import admin
from django.urls import path
from tours import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='index'),
    path('departure/<str:departure>/', views.departure_view, name='departure_view'),
    path('tour/<int:id>/', views.tour_view, name='tour_view'),
]

handler404 = views.custom_handler404
