from .models import Orgnisation
from championship.models import Team
from django import forms

class team_member_management(forms.ModelForm):
	
	class Meta:
		model = Team
		fields = ('playerList',)