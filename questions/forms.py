from django import forms

from .models import Test, Question


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded p-2'
            }),
            'lesson': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded p-2'
            })
        }
