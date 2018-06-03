from django.http import HttpResponse
from django.shortcuts import render
from championship.forms import AddChsForm
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
