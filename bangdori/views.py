from tkinter import TRUE
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from django.views import View
from bangdori.models import CustomerUser, Authentication
import os
import json
import requests
import time
import random
from django.http import JsonResponse
from .utils import make_signature
load_dotenv()
# Create your views here.


def goIndex(request):
    return redirect('index')


def index(request):
    user_pk = request.session.get('user')
    username = {}
    if user_pk:
        user = CustomerUser.objects.get(pk=user_pk)
        username['user_id'] = user.userid
        username['user_email'] = user.email
        username['user_birth'] = user.birthday
        username['user_phone'] = user.phone
        username['user_logged_in'] = TRUE

    return render(request, 'index.html', username)


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        context = {}

        user_id = request.POST.get('login_user_id')
        passwd = request.POST.get('login_user_pwd')

        if not (user_id and passwd):
            context['error'] = "빈칸없이 입력해주세요."
        else:
            user = CustomerUser.objects.get(userid=user_id)
            if check_password(passwd, user.passwd):
                request.session['user'] = user.userid
                return redirect('/index')
            else:
                context['error'] = "비밀번호가 틀렸습니다."
    return render(request, 'login.html', context)


def logout(request):
    if request.session['user']:
        del (request.session['user'])
    return redirect('/index')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        context = {}
        user_id = request.POST.get('register_user_id', None)
        passwd = request.POST.get('register_user_pwd', None)
        passwd2 = request.POST.get('register_user_repwd', None)
        email_id = request.POST.get('register_user_email_id', None)
        email_net = request.POST.get('register_user_email', None)
        year = request.POST.get('register_user_year', None)
        month = request.POST.get('register_user_month', None)
        day = request.POST.get('register_user_day', None)
        phone = request.POST.get('register_user_phone', None)
        if not (user_id and passwd and passwd2 and email_id and email_net
                and year and month and day and phone):
            context['error'] = "빈칸없이 입력해주세요."
        elif passwd != passwd2:
            context['error'] = "비밀번호가 다릅니다."
        else:
            birth = year + month + day
            email = email_id + "@" + email_net
            user = CustomerUser(
                userid=user_id,
                passwd=make_password(passwd),
                email=email,
                birthday=birth,
                phone=phone,
            )
            user.save()
            return redirect('/login')

        return render(request, 'register.html', context)


def dabang(request):
    return render(request, 'dabang.html')


def succession(request):
    return render(request, 'succession.html')


def essentials(request):
    return render(request, 'essentials.html')


def group(request):
    return render(request, 'group.html')


def board(request):
    return render(request, 'board.html')


def notice(request):
    return render(request, 'notice.html')


def contact(request):
    return render(request, 'contact.html')


def write(request):
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
            'https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:292652557635:sms_auth/messages', headers=headers, data=body)

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
        if(auth_mobile.auth_number == message):
            user_id = CustomerUser.objecvts.filter(
                phone=input_mobile_num).alues('userid')
            if(user_id):
                return JsonResponse({'message': str(user_id)}, status=200)
            else:
                return JsonResponse({'message': 'Not User!'}, status=200)
        else:
            return JsonResponse({'message': 'Not Correct Number!'}, status=200)
