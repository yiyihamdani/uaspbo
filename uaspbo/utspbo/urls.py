"""latihan2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app_utspbo.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('halamanjurnal/', halamanjurnal),
    path('halamandetail/', halamandetail),
    path('halamanjurnal/<int:id>', detail, name='data_jurnal'),
    path('tambahjurnal/', tambahjurnal),
    path("halamanjurnal/updatejurnal/<int:id_Jurnal>", updatejurnal, name = 'updatejurnal'),
    path("halamanjurnal/deletejurnal/<int:id_Jurnal>", deletejurnal, name = 'deletejurnal'),
]