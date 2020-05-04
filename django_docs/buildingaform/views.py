from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

# Create your views here.


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