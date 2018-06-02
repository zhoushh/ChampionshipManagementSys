from django import forms
from .models import Championship


class AddChsForm(forms.ModelForm):
	
	range_choices = (
		('national', '国家级'),
		('regional', '地区级'),
		('local', '地方级')
	)
	
	type_choice = (
		('league', '联赛'),
		('cup', '杯赛')
	)
	
	chsCode = forms.CharField()
	chsName = forms.CharField()
	chsRange = forms.ChoiceField(choices=range_choices)
	chsType = forms.ChoiceField(choices=type_choice)
	chsCapacity = forms.IntegerField()
	chsStartDate = forms.DateField()
	chsEndDate = forms.DateField()
	
	class Meta:
		model = Championship
		fields = ('chsCode', )
		
		