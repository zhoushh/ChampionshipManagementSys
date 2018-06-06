from django.shortcuts import render
from django.http import HttpResponse
from championship.forms import AddChsForm
from .models import Championship
from collections import deque
import random
# Create your views here.


#改至orgnisation.models中实现
# def chs_add(request):
# 	if request.method == 'GET':
# 		add_chs_form = AddChsForm()
# 		return render(request, 'championship/add_chs.html', {'form': add_chs_form})
# 	if request.method == 'POST':
# 		add_chs_form = AddChsForm(request.POST)
# 		if add_chs_form.is_valid():
# 			new_chs = add_chs_form.save()
# 			new_chs.save()
# 			print('chs added')
# 			return HttpResponse('success')


def generate_timetable(request, org_id, chs_id, chs_cap):
	
	def setup_schedule(team_list):
		schedule = dict.fromkeys(range(1, int(chs_cap)))
		core_position = team_list[0]
		ring = team_list[1:]
		ring = deque(ring)
		# 前半赛程，1-19轮(round)
		for round in range(1, int(chs_cap)):
			# 第一支球队不动，再加上轮转(rotate)的环
			teams = [core_position] + list(ring)
			# 切成2列，左边主队，右边客队
			# 使用//运算符使除法运算结果为整型
			home, away = teams[:len(teams) // 2], teams[len(teams) // 2:]
			away = away[::-1]
			# 随机打乱主客队
			schedule[round] = [(x, y) if random.random() >= 0.5 else (y, x) for x, y in zip(home, away)]
			ring.rotate(1)
		 # 若双循环则后半赛季主客对调，暂不使用
		 # for round in range(20, 39):
		 # 	schedule[round] = [(y, x) for x, y in schedule[round - 19]]
		return schedule
	
	chs_to_arrange = Championship.objects.get(pk=chs_id)
	team_list = chs_to_arrange.team_list.split(',')
	schedule = setup_schedule(team_list)
	
	return HttpResponse(schedule)
	