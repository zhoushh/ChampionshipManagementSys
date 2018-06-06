from .models import Orgnisation
from championship.models import Team
from django import forms

class TeamMemberManagement(forms.ModelForm):
	
	class Meta:
		model = Team
		fields = ('playerList',)
		
		
class AddTeamForm(forms.ModelForm):
	
	class Meta:
		model = Team
		fields = ('teamType', 'teamName', 'belongTo', )