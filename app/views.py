from django.shortcuts import render, redirect

# Create your views here.

def goIndex(request):
    return redirect('index')

def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')

def dabang(request):
    return render(request, 'app/dabang.html')

def succession(request):
    return render(request, 'app/succession.html')

def essentials(request):
    return render(request, 'app/essentials.html')

def group(request):
    return render(request, 'app/group.html')
    
def board(request):
    return render(request, 'app/board.html')

def notice(request):
    return render(request, 'app/notice.html')

def contact(request):
    return render(request, 'app/contact.html')

def write(request):
    return render(request, 'app/write.html')

def findID(request):
    return render(request, 'app/findID.html')

def findPW1(request):
    return render(request, 'app/findPW1.html')

def findPW2(request):
    return render(request, 'app/findPW2.html')