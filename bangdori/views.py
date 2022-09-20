from tkinter import TRUE
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

from bangdori.models import CustomerUser


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


def findPW1(request):
    return render(request, 'findPW1.html')


def findPW2(request):
    return render(request, 'findPW2.html')