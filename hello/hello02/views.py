from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello02.html', {'name': '파이썬'})

def var01(request):
    lst = ['Python', 'Django', 'Template']
    return render(request, 'variable01.html', {'lst': lst})

def var02(request):
    dct = {'class':'qclass' , 'name':'홍길동' }
    return render(request, 'variable02.html', {'dct': dct})