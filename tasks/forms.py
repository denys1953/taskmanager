from django import forms
from .models import Task

class BaseTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority', 'description']
        widgets = {
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }

class TaskCreateForm(BaseTaskForm):
    pass

class TaskUpdateForm(BaseTaskForm):
    pass
