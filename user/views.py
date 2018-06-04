from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.http import HttpResponse
from .forms import LoginForm
from .forms import RegistrationForm
from article.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
	articles = Article.objects.all()
	paginator = Paginator(articles, 6)
	page = request.GET.get('page', 1)
	try:
		send_articles = paginator.page(page)
	except EmptyPage:
		send_articles = paginator.page(paginator.num_pages)

	
	
	# page = request.GET.get('page')
	# if page:
	# 	articles = Paginator.page(page).object_list
	# else:
	# 	articles =Paginator.page(1).object_list
	# try:
	# 	articles = Paginator.page(page)
	# except PageNotAnInteger:
	# 	articles = Paginator.page(1)
	# except EmptyPage:
	# 	articles = Paginator.page(Paginator.num_pages)
		
	
	return render(request, 'index.html', {'articles': send_articles})


def loginView(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user:
				login(request, user)
				print("login succeeded")
				if user.userType == 'association':
					return render(request, 'orgnisation/org_index.html')
				elif user.userType == 'club':
					return HttpResponse('club user logged')
				else:
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
