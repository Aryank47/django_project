"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from home.views import home_view,design,form2,form1,carousel

urlpatterns = [
	path('',home_view),
    path('form2/', form2),
    path('carousel/', carousel),
    path('form1/', form1),
    path('design/',design),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
