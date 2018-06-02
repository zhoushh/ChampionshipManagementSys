from django.shortcuts import render

# Create your views here.


def org_index(request):
	return render(request, 'orgnisation/org_index.html')


def org_operate(request):
	return render(request, 'orgnisation/org-operate.html')


def org_add_chs(request):
	return render(request, 'championship/add_chs.html')
