from django import forms
from django.core.exceptions import ValidationError

from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded p-2'
            }),
            'desc': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded p-2'
            }),
        }

    def clean_name(self):
        names = self.cleaned_data['name'].split()
        for name in names:
            if not name.isalpha():
                raise ValidationError('Name must contain only letters.')
        return self.cleaned_data['name']
