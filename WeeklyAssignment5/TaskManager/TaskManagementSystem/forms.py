from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    group= forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label='Group')

    class Meta:
        model=User
        fields=['username','password1','password2','group']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Username'
        self.fields['password1'].label='Password'
        self.fields['password2'].label='Password confirmation'
