from django.shortcuts import render
from championship.forms import AddChsForm
# Create your views here.


def org_index(request):
	return render(request, 'orgnisation/org_index.html')


def org_operate(request):
	return render(request, 'orgnisation/org-operate.html')


def org_add_chs(request):
	add_chs_form = AddChsForm()
	return render(request, 'championship/add_chs.html', {'form': add_chs_form})
