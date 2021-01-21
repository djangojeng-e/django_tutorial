from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import NameForm

# Create your views here.


def index(request):
    print(request.session)
    print(dir(request.session))
    # request.session['fav_color'] = 'red'
    # print(request.session.keys())
    # print(request.session.__getitem__('fav_color'))
    # print(request.session.__contains__('fav_color'))
    print(request.session.keys())
    print(request.session.values())
    # print(request.session.set_test_cookie())
    # print(request.session.test_cookie_worked())
    # print(request.session.delete_test_cookie())
    print(request.session.get_session_cookie_age())
    print(request.session.flush())
    return HttpResponse('This is a index page')


def get_name(request):
    if request.method == "POST":
        # 폼 인스턴스를 생성, 요청으로 받아온 데이터로 채웁니다
        form = NameForm(request.POST)
        # 유효한 데이터인지 검사
        if form.is_valid():
            # form.cleaned_data 안에 있는 데이터를 요구사항에 맞게 처리
            # ...
            # 새로운 URL 로 리다이렉트 시켜줌
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})