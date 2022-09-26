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
    success_url = reverse_lazy('profileapp:view')
    template_name = 'create.html'

    def form_valid(self, form):  # ProfileCreationForm의 data가 2번째 파라미터에 들어 있어요.
        temp_profile = form.save(commit=False)  # 임시로 저장함.<commit=False> 키워드 인자를 이용해서
        temp_profile.user = self.request.user
        temp_profile.save()# self는 view에서 가져온 self임. 또, 웹브라우저에서 입력 받은 값이 우항 좌항이 db에서 가져온값
        return super().form_valid(form)
def view(request):
    return render(request, 'view.html')