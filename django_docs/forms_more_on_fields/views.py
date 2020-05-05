from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.forms import forms


# Create your views here.


from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactForm

# Create your views here.


def get_form(request):
    if request.method == "POST":
        # 폼 인스턴스를 생성, 요청으로 받아온 데이터로 채웁니다
        form = ContactForm(request.POST)
        # 유효한 데이터인지 검사
        if form.is_valid():
            # form.cleaned_data 안에 있는 데이터를 요구사항에 맞게 처리
            # ...
            # 새로운 URL 로 리다이렉트 시켜줌
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contactform.html', {'form': form})


#
# if form.is_valid():
#     subject = form.cleaned_data['subject']
#     message = form.cleaned_data['message']
#     sender = form.cleaned_data['sender']
#     cc_myself = forms.cleaned_data['cc_myself']
#
#     recipients = ['info@example.com']
#
#     if cc_myself:
#         recipients.append(sender)
#
#     send_mail(subject, message, sender, recipients)
#     return HttpResponseRedirect('/thanks/')