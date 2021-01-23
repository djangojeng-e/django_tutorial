from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    print(request.session)
    print(dir(request.session))
    print(request.session.keys())
    print(request.session.values())
    request.session['django'] = 'Session'
    print(request.session.keys())
    print(request.session.values())
    return HttpResponse('이것은 index 뷰 입니다')