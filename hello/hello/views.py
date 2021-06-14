from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def mytest(request):
    return HttpResponse('<h1>Hello, Django!</h1>')