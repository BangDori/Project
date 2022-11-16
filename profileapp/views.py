from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

import bangdori
from bangdori.models import CustomerUser
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
        temp_profile.save()  # self는 view에서 가져온 self임. 또, 웹브라우저에서 입력 받은 값이 우항 좌항이 db에서 가져온값
        return super().form_valid(form)


def view(request):
    return render(request, 'view.html')


def profile(request):
    return render(request, 'profile.html')


def mypage(request):
    return redirect('profileapp:myinfo')


def myinfo(request):
    """
    내 정보
    """
    return render(request, 'myinfo.html')


def mypost(request):
    """
    내가 쓴 글
    """
    return render(request, 'mypost.html')


def favorites(request):
    """
    즐겨찾기
    """
    return render(request, 'favorites.html')


def settings(request):
    """
    설정
    """
    return render(request, 'settings.html')


class Address(View):
    def get(self, request):
        if request.user.is_anonymous:
            # 로그인되지 않은 상태
            return redirect(reverse('index'))

        # 주소 등록 페이지
        return render(request, 'address.html')

    def post(self, request):
        # 주소 모델 생성
        addr = bangdori.models.Address()
        try:
            addr.postcode = int(request.POST.get('postcode'))
        except:
            pass

        addr.road = request.POST.get('road')
        addr.lot = request.POST.get('lot')
        addr.detail = request.POST.get('detail')
        addr.extra = request.POST.get('extra')
        addr.city = request.POST.get('sido')
        addr.state = request.POST.get('sigungu')
        addr.road_name = request.POST.get('roadname')
        addr.lat = float(request.POST.get('lat'))
        addr.lng = float(request.POST.get('lng'))
        # 주소 모델 저장
        addr.save()

        # 사용자 모델 가져옴
        user: CustomerUser = request.user
        # 이미 등록되어 있으면 해당 데이터를 삭제하고 저장
        if user.addr:
            user.addr.delete()

        # 저장
        user.addr = addr
        user.save()
        return render(request, 'address.html')
