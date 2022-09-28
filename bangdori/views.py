from tkinter import TRUE

from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView
from dotenv import load_dotenv
from django.views import View

from project.settings import MAX_ARTICLES
from .models import *
import os, json, requests, time, random
from django.http import JsonResponse
from .utils import make_signature, getModelByName

load_dotenv()


# Create your views here.

def goIndex(request):
    return redirect('index')


def index(request):

    
    context = {}
    """ 
    로그인 정보는 Session에 기록되도록 설정되어 있음.
    dict 형식으로 request 전달 비활성화
    """
    # logged_user = request.session.get('user')
    # print(logged_user)
    # logged_user = {}
    # if logged_user:
    #     user = CustomerUser.objects.get(username=username)
    #     username['username'] = user.username
    #     username['user_email'] = user.email
    #     username['user_birth'] = user.birthday
    #     username['user_phone'] = user.phone
    #     username['user_logged_in'] = TRUE

    return render(request, 'index.html', {})


def login(request):
    # 기본이 POST로 수정
    if request.method == "POST":
        context = {}
        # AuthenticationForm으로부터 인증 Form을 받아옴
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            # cleaned_data 형식으로 아이디와 비밀번호를 가져옴
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Django의 auth 클래스를 사용해 로그인
            user = auth.authenticate(request=request, username=username, password=password)

            # 해당하는 유저가 존재해서 로그인이 가능한 경우
            if user is not None:
                auth.login(request, user)
                return redirect('/index')

        """
        DB에서 Filter를 이용하지 않고, auth 클래스를 이용하여 로그인하도록 수정함
        오류 메시지는 아직 구현되지 않음
        """
        # if not (username and password):
        #     context['error'] = "빈칸없이 입력해주세요."
        # else:
        #     if CustomerUser.objects.filter(username=username):
        #         user = CustomerUser.objects.get(username=username)
        #         if check_password(password, user.password):
        #             request.session['user'] = user.username
        #             return redirect('/index')
        #         else:
        #             context['error'] = "해당 회원정보가 존재하지 않습니다."
        #     else:
        #         context['error'] = "해당 회원정보가 존재하지 않습니다."
    else:
        return render(request, 'login.html')

    return render(request, 'login.html', context)


def logout(request):
    # del 방식을 이용하지 않고, auth에서 제공하는 메서드를 이용
    auth.logout(request)
    return redirect('/index')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # register로 POST 요청이 들어오면, 새로운 User를 생성하는 절차
        context = {}

        username = request.POST.get('register_username', None)
        password = request.POST.get('register_user_pwd', None)
        password2 = request.POST.get('register_user_repwd', None)
        email_id = request.POST.get('register_user_email_id', None)
        email_net = request.POST.get('register_user_email', None)
        year = request.POST.get('register_user_year', None)
        month = request.POST.get('register_user_month', None)
        day = request.POST.get('register_user_day', None)
        phone = request.POST.get('register_user_phone', None)

        # 중복 확인 구현할 것
        if CustomerUser.objects.filter(username=username).exists():
            context['error'] = "사용할 수 없는 ID입니다."

        if password != password2:
            context['error'] = "비밀번호가 다릅니다."
        elif not (username and password and password2 and email_id and email_net
                  and year and month and day and phone):
            context['error'] = "빈칸없이 입력해주세요."
        else:
            user = CustomerUser.objects.create_user(username=username,
                                                    password=password2,
                                                    email=f'{email_id}@{email_net}',
                                                    birthday=f'{year}-{month}-{day}',
                                                    phone=phone)
            auth.login(request, user)
            return redirect('/')

        return render(request, 'register.html', context)

class DetailView(DetailView):
    model = CustomerUser
    context_object_name = 'target_user'
    template_name = 'view.html'

def dabang(request):
    return render(request, 'dabang.html')


def succession(request):
    return render(request, 'succession.html')


def essentials(request):
    return render(request, 'essentials.html')


def group(request):
    return render(request, 'group.html')


def board(request, name):
    """
    board : 게시판 목록을 보여주는 view
    """

    # 페이지에 넘겨줄 Context
    context = {}

    # 게시판 내용 불러올 Article 객체
    articles = getModelByName(name)

    # 페이지 정보 전달
    # context['name'] : 페이지가 표시되는 한글 이름
    context['name'] = articles._meta.verbose_name
    # context['url'] : 페이지에서 url로 전달받은 이름
    context['url'] = name

    # 모든 글 가져옴, 날짜 내림차순으로 조회
    articles = articles.objects.all().order_by('-date')
    # Paginator 사용
    paginator = Paginator(articles, MAX_ARTICLES)
    # GET 요청이 들어오면 page 파라미터를 읽어옴
    page = int(request.GET.get('page', 1))

    # 현재 페이지에 맞는 게시물 목록을 Context로 넘겨줌
    context['articles'] = paginator.get_page(page)

    return render(request, 'board.html', context)


def notice(request):
    return render(request, 'notice.html')


def contact(request):
    return render(request, 'contact.html')


def article(request, name, pk):
    """
    article : 게시글 내용을 보여주는 view
    """

    context = {}

    # 게시글 정보 불러옴
    article = getModelByName(name)
    article = article.objects.all().get(id=pk)

    # 조회수 올림
    article.views = article.views + 1
    article.save()

    # Context에 전달
    context['url'] = name
    # Context에 게시글 정보 추가
    context = {**context, **article.__dict__()}

    print(context)
    return render(request, 'article.html', context)


def write(request, name):
    """
    write : 게시글을 작성하는 view
    """

    # 현재 로그인된 사용자의 정보를 가져옴
    user = request.user

    if request.method == "POST":
        # 현재 게시판에 맞는 모델을 가져옴
        article = getModelByName(name)
        # 게시글 작성
        article = article(title=request.POST.get('title'),
                          writer=CustomerUser.objects.get(username=user),
                          content=request.POST.get('content'))

        # 게시글 저장
        article.save()
        # 게시판으로 다시 돌아감
        return redirect('board', name=name)

    return render(request, 'write.html')


def findID(request):
    return render(request, 'findID.html')


def SMS(request):
    return render(request, 'temp_sms.html')


def findPW1(request):
    return render(request, 'findPW1.html')


def findPW2(request):
    return render(request, 'findPW2.html')


class SmsSendView(View):
    def send_sms(self, phone_number, auth_number):
        timestamp = str(int(time.time() * 1000))
        headers = {
            'Content-Type': "application/json; charset=UTF-8",
            'x-ncp-apigw-timestamp': timestamp,
            'x-ncp-iam-access-key': os.getenv('ncloud_private_Accesskey'),
            'x-ncp-apigw-signature-v2': make_signature(timestamp)
        }
        body = {
            "type": "SMS",
            "contentType": "COMM",
            # 사전에 등록해놓은 발신용 번호 입력, 타 번호 입력시 오류
            "from": os.getenv('call_number'),
            "content": f"[강병준 씹새야:{auth_number}]",  # 메세지를 이쁘게 꾸며보자
            "messages": [{"to": f"{phone_number}"}]
        }
        body = json.dumps(body)
        requests.post(
            'https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:292652557635:sms_auth/messages', headers=headers,
            data=body)

    def post(self, request):
        # data = json.loads(request.body)
        print('dd')
        try:
            input_mobile_num = request.POST['phone_number']
            auth_num = random.randint(10000, 100000)  # 랜덤숫자 생성, 5자리로 계획하였다.
            auth_mobile = Authentication.objects.get(
                phone_number=input_mobile_num)
            auth_mobile.auth_number = auth_num
            auth_mobile.save()
            self.send_sms(
                phone_number=input_mobile_num, auth_number=auth_num)
            return JsonResponse({'message': 'Complete 발송완료'}, status=200)
        except:  # 인증요청번호 미 존재 시 DB 입력 로직 작성
            Authentication.DoesNotExist
            Authentication.objects.create(
                phone_number=input_mobile_num,
                auth_number=auth_num,
            ).save()
            self.send_sms(phone_number=input_mobile_num, auth_number=auth_num)
            return JsonResponse({'message': '인증번호 발송 및 DB 입력완료'}, status=200)


class SmsVerifyView(View):
    def post(self, request):
        input_mobile_num = request.POST['phone_number']
        message = request.POST['message_number']

        auth_mobile = Authentication.objects.get(
            phone_number=input_mobile_num)
        if (auth_mobile.auth_number == message):
            username = CustomerUser.objecvts.filter(
                phone=input_mobile_num).alues('username')
            if (username):
                return JsonResponse({'message': str(username)}, status=200)
            else:
                return JsonResponse({'message': 'Not User!'}, status=200)
        else:
            return JsonResponse({'message': 'Not Correct Number!'}, status=200)
