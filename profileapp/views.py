from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from .decorator import profile_ownership_required
from .forms import ProfileCreateForm
from .models import Profile

# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('view.html')
    template_name = 'create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profileapp:create')
