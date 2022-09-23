from django.forms import ModelForm

from .models import Profile


class ProfileCreateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname']
