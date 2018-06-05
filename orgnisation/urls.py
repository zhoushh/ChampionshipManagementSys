from django.urls import path,include,re_path
from . import views
from article.views import org_create_article
from django.contrib.auth import views as authViews

app_name = 'orgnisation'

urlpatterns = [
	path("orgIndex/", views.org_index, name='orgIndexView'),
	path("orgOperation/", views.org_operate, name='orgOperationView'),
	path("add_chs/", views.org_add_chs, name='org_add_chs'),
	path("create_article/", org_create_article, name='org_create_article'),
	path("club_index/", views.org_club_index, name='org_club_index'),
	path("club_operate/<org_id>", views.club_operate, name='org_club_operate'),
	path("club_operate/<org_id>/player_list/<team_id>", views.club_team_list_operate, name='team_player_list_op'),
	path("club_operate/<org_id>/add_team", views.club_add_team, name='club_add_team'),
]