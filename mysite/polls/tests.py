from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() 가 pub_date 가 미래 날짜로 지정되어 있는
        질문들에 대해서 False 를 반환함
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() 가 pub_date 가 1일이상 되었을때
        False 를 반환합니다
        :return:
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recenlty_with_recent_question(self):
        """
        was_published_recently() 가 pub_date 가 어제 이전이면,
        True 를 반환합니
        :return:
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)