from django import forms
from django.forms import ClearableFileInput, FileInput
from .models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
        widgets = {
            'image': FileInput(attrs={
                'class':'pt_btn1',
            }),
        }