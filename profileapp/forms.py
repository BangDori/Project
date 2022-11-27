from django import forms
from django.forms import ClearableFileInput, FileInput, ModelForm, TextInput
from .models import Profile

class ProfileCreateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'image': FileInput(attrs={
                'class':'pt_btn1',
            }),
        }