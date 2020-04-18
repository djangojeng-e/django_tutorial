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