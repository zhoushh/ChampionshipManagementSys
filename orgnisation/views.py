from django.http import HttpResponse
from django.shortcuts import render
from championship.forms import AddChsForm
from .forms import TeamMemberManagement, AddTeamForm
from .models import Orgnisation
from championship.models import Team
import csv
# Create your views here.


def org_index(request):
	return render(request, 'orgnisation/org_index.html')


def org_operate(request):
	return render(request, 'orgnisation/org-operate.html')


def org_add_chs(request):
	if request.method == 'GET':
		add_chs_form = AddChsForm()
		return render(request, 'championship/add_chs.html', {'form': add_chs_form})
	if request.method == 'POST':
		add_chs_form = AddChsForm(request.POST)
		if add_chs_form.is_valid():
			add_chs_form.save()
			print('chs added')
			return HttpResponse('success')
		else:
			return HttpResponse('error')
		
		
def org_club_index(request):
	return render(request, 'org_club/club_index.html')


def club_operate(request, org_id):
	#放弃了在这个view函数中处理team的form
	# if request.method == 'GET':
	# 	player_management_form = team_member_management()
		club_org = Orgnisation.objects.get(pk=org_id)
		teams_belong_to_this = Team.objects.filter(belongTo_id=org_id)
		return render(request, 'org_club/club_operate.html', {'club': club_org, 'teams': teams_belong_to_this})
	# if request.method == 'POST':
	# 	player_management_form = team_member_management(request.POST)
	# 	org_club = Orgnisation.objects.get(pk=org_id)
	# 	if player_management_form.is_valid():
	# 		player_management_form.save()
	# 		return HttpResponse('success')
	# 	else:
	# 		return HttpResponse('error')
	
	
def club_team_list_operate(request, org_id, team_id):
	if request.method == 'GET':
		player_list_form = TeamMemberManagement()
		team_to_check = Team.objects.get(pk=team_id)
		return render(request, 'org_club/team_operate.html', {'player_list_form': player_list_form, 'team_selected': team_to_check})
	if request.method == 'POST':
		player_list_form = TeamMemberManagement(request.POST)
		team_to_check = Team.objects.get(pk=team_id)
		org_club = Orgnisation.objects.get(pk=org_id)
		if team_to_check.belongTo == org_club.id:
			if player_list_form.is_valid():
				player_list_form.save()
				return HttpResponse('success')
			else:
				return HttpResponse('error')
		else:
			return HttpResponse('club and team do not match. ')
		
		
def club_add_team(request, org_id):
	if request.method == 'GET':
		add_team_form = AddTeamForm()
		return render(request, 'org_club/club_add_team.html', {'add_team_form': add_team_form})
	if request.method == 'POST':
		add_team_form = AddTeamForm(request.POST or None, request.FILES or None)
		add_team_form.belongTo = Orgnisation.objects.get(pk=org_id)
		if add_team_form.is_valid():
			add_team_form.save()
			print('team added')
			return HttpResponse('success')
		else:
			return HttpResponse('error')