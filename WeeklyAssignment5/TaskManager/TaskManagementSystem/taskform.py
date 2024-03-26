from django import forms 
from .models import Task
from django.contrib.auth.models import Group

class TaskCreationForm(forms.ModelForm):

    group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None)
    class Meta:
        model=Task
        fields=['title','description','group','complete']


    def __init__(self, *args, **kwargs):
        super(TaskCreationForm, self).__init__(*args, **kwargs)
        # Add a dropdown field for selecting the group
        self.fields['group'].widget = forms.Select(choices=Group.objects.all().values_list('id', 'name'))