from django.urls import path,include,re_path
from . import views
from django.contrib.auth import views as authViews

app_name = 'orgnisation'

urlpatterns = [
	path("orgIndex/", views.org_index, name='orgIndexView'),
	path("orgOperation/", views.org_operate, name='orgOperationView'),
	path("add_chs", views.org_add_chs, name='org_add_chs')
]