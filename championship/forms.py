from django import forms
from .models import Championship


class AddChsForm(forms.ModelForm):
	
	class Meta:
		model = Championship
		fields = ('chsName', 'chsType', 'capacity', 'range', 'startTime', 'endTime')