from django.urls import path,include,re_path
from . import views

app_name = 'article'

urlpatterns = [
	path("view_article/<article_id>", views.view_article, name="view_article")
]