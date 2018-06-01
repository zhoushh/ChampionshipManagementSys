from django.shortcuts import render

# Create your views here.

def org_index(request):
	return render(request, 'orgnisation/org_index.html')


