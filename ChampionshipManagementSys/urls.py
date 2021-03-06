"""ChampionshipManagementSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic import TemplateView
from django.urls import path, include, re_path
import user.views as uv
from ChampionshipManagementSys.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', uv.index, name='index'),
	path('user/', include('user.urls', namespace='user')),
	path('org/', include('orgnisation.urls', namespace='org')),
	#path('chs/', include('championship.urls', namespace='chs'))
	path('article/', include('article.urls', namespace='article')),
	re_path(r'^gfile/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}, name='down'),

]
