"""webwing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Appwebwing import views
from webwing import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('courses',views.courses,name='courses'),
    path('contact',views.contact,name='contact'),
    path('contact_save',views.contact_save,name='contact_save'),
    # path('pricing',views.pricing,name='pricing'),
]

 # +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
