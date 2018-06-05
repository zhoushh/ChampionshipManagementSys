from django.shortcuts import render
from django.http import HttpResponse
from championship.forms import AddChsForm
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