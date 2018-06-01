from django import forms
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名：')
    password = forms.CharField(label='密码：', widget=forms.PasswordInput)
    
    
class RegistrationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(label='输入密码：', widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(label='确认密码：', widget=forms.PasswordInput)
    
    class Meta:
        model = UserProfile
        fields = ('username',)
        
    def check_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['passwordConfirm']:
            raise forms.ValidationError("密码两次不一致")
        return cd['password']