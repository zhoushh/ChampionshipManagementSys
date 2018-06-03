from .models import Article
from django import forms

class OrgCreateArticleForm(forms.ModelForm):
	
	class Meta:
		model = Article
		fields = ('title', 'content')