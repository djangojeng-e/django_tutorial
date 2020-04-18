from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """가장 최근의 5개의 발행된 질문들을 반환"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        아직 발행되지 않은 질문들을 제외합니다.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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

