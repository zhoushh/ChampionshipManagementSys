from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.http import HttpResponse
from .forms import LoginForm
from .forms import RegistrationForm


# Create your views here.


def index(request):
	return render(request, 'index.html')


# def loginView(request):
#     if request.method == 'POST':
#         print('POST')
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = authenticate(username = username, password = password)
#         if user :
#             login(request, user)
#             return render(request, 'index.html')
#
#     return render(request, 'user/login.html')

def loginView(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user:
				login(request, user)
				print("login succeeded")
				return render(request, 'index.html')
			else:
				return HttpResponse("Sorry. Your username or password is not correct.")
		else:
			return HttpResponse("Invalid login")
	
	if request.method == 'GET':
		login_form = LoginForm()
		return render(request, 'user/login.html', {'form': login_form})


def registerView(request):
	if request.method == 'POST':
		regForm = RegistrationForm(request.POST)
		if regForm.is_valid():
			newUser = regForm.save(commit=False)
			newUser.set_password(regForm.cleaned_data['password'])
			newUser.save()
			print('user registed')
			return render(request, 'index.html')
		else:
			return HttpResponse('sorry, errors occur, please contact administrator')
	
	else:
		regForm = RegistrationForm()
		return render(request, 'user/register.html', {'form': regForm})
