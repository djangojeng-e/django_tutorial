from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 투표 폼을 다시 출력
        return render(request, 'polls/detail.html',
                  {'question': question,
                   'error_message': "You didn't select a choice",
                    })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 항상 POST 데이터를 성공적으로 다루었을때는
        # HttpResponseRedirect 를 반환해 줍니다
        # 이것으로 사용자가 데이터를 뒤로가기 버튼을 눌러서 데이터를 두번 전송하는것을 방지합니다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

