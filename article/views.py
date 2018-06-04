from django.shortcuts import render
from .forms import OrgCreateArticleForm
from django.http import HttpResponse
from .models import Article
# Create your views here.


def org_create_article(request):
	if request.method == 'GET':
		org_create_article_form = OrgCreateArticleForm()
		return render(request, 'article/org_add_article.html', {'form': org_create_article_form})
	if request.method == 'POST':
		org_create_article_form = OrgCreateArticleForm(request.POST)
		if org_create_article_form.is_valid():
			org_create_article_form.save()
			print('article created')
			return HttpResponse('ok')
		else:
			return HttpResponse('error')
		
		
def view_article(request, article_id):
	article = Article.objects.get(pk=article_id)
	return  render(request, 'article/view_article.html', {'article': article})
