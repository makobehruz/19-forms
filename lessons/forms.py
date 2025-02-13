from django import forms

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